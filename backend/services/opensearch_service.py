"""OpenSearch retrieval service."""

from __future__ import annotations

import logging
import time
from typing import Any

from backend.models.schemas import (
    DebugInfo,
    QueryFilters,
    QueryOptions,
    RetrievedChunk,
)
from backend.services.embedding_service import embed_query_titan
from backend.services.reranking_service import rerank

logger = logging.getLogger(__name__)


def _build_os_filter(filters: QueryFilters) -> list[dict]:
    """Build an OpenSearch bool-filter clause list for flat keyword fields."""
    clauses: list[dict] = []
    if filters.status:
        clauses.append({"term": {"status": filters.status}})
    if filters.entity:
        clauses.append({"term": {"entity": filters.entity}})
    if filters.document_type:
        clauses.append({"term": {"document_type": filters.document_type}})
    return clauses


def _hit_to_chunk_dict(hit: dict) -> dict:
    """Convert an OpenSearch hit to a flat dict suitable for RetrievedChunk.

    OpenSearch stores flat fields (no nested source object) — the field
    associations for people/fees are already lost at this point.
    """
    src = hit.get("_source", {})
    # Reconstruct people_mentioned from parallel arrays (lossy)
    person_names = src.get("person_names", [])
    person_roles = src.get("person_roles", [])
    person_entities = src.get("person_entities", [])
    people = [
        {"name": n, "role": r, "entity": e}
        for n, r, e in zip(person_names, person_roles, person_entities)
    ] if person_names else []

    return {
        "content": src.get("content", ""),
        "source_title": src.get("document_title", ""),
        "source_date": src.get("published_date"),
        "source_entity": src.get("entity"),
        "source_status": src.get("status"),
        "document_type": src.get("document_type"),
        "section": src.get("section"),
        "fiscal_year": src.get("fiscal_year"),
        "version": src.get("version"),
        "superseded_by": None,  # not stored in flat mapping
        "people_mentioned": people,
        "product_info": (
            {"product_name": src["product_name"], "product_category": src.get("product_category")}
            if src.get("product_name")
            else None
        ),
        "score": hit.get("_score", 0.0),
    }


def _rrf_merge(
    vector_hits: list[dict],
    text_hits: list[dict],
    k: int = 60,
) -> list[dict]:
    """Reciprocal Rank Fusion of two OpenSearch hit lists."""
    scores: dict[str, float] = {}
    hit_map: dict[str, dict] = {}

    for rank, hit in enumerate(vector_hits):
        doc_id = hit["_id"]
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
        hit_map[doc_id] = hit

    for rank, hit in enumerate(text_hits):
        doc_id = hit["_id"]
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
        if doc_id not in hit_map:
            hit_map[doc_id] = hit

    sorted_ids = sorted(scores, key=lambda x: scores[x], reverse=True)
    merged = []
    for doc_id in sorted_ids:
        hit = hit_map[doc_id].copy()
        hit["_score"] = scores[doc_id]
        merged.append(hit)
    return merged


async def query_opensearch(
    question: str,
    filters: QueryFilters,
    options: QueryOptions,
    os_client: Any,
) -> tuple[list[RetrievedChunk], DebugInfo]:
    """Run a kNN (+ optional hybrid) search against OpenSearch.

    Parameters
    ----------
    question : str
        Natural language query.
    filters : QueryFilters
        Optional metadata filters.
    options : QueryOptions
        Search options (hybrid, reranking, embedding mode, etc.).
    os_client : OpenSearch
        The opensearch-py client stored in app.state.

    Returns
    -------
    tuple[list[RetrievedChunk], DebugInfo]
    """
    index_name = "bank_chunks"
    t_start = time.perf_counter()

    # ── 1. Embed query with Titan ─────────────────────────────────────────
    query_vector = await embed_query_titan(question)

    # ── 2. Build filter clauses ───────────────────────────────────────────
    filter_clauses = _build_os_filter(filters)

    # ── 3. kNN vector search with Lucene engine efficient filtering ───────
    knn_body: dict[str, Any] = {
        "size": 20,
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_vector,
                    "k": 20,
                }
            }
        },
    }

    if filter_clauses:
        knn_body["query"]["knn"]["embedding"]["filter"] = {
            "bool": {"must": filter_clauses}
        }

    import asyncio

    vector_response = await asyncio.to_thread(
        os_client.search, body=knn_body, index=index_name
    )
    vector_hits: list[dict] = vector_response.get("hits", {}).get("hits", [])
    candidates_before = vector_hits.__len__()

    t_retrieval = time.perf_counter()

    # ── 4. Optional hybrid: separate text match + manual RRF ──────────────
    hybrid_used = False
    combined_hits = vector_hits

    if options.use_hybrid_search:
        hybrid_used = True
        text_body: dict[str, Any] = {
            "size": 20,
            "query": {
                "bool": {
                    "must": [
                        {"match": {"content": question}},
                    ],
                }
            },
        }
        if filter_clauses:
            text_body["query"]["bool"]["filter"] = filter_clauses

        text_response = await asyncio.to_thread(
            os_client.search, body=text_body, index=index_name
        )
        text_hits: list[dict] = text_response.get("hits", {}).get("hits", [])

        combined_hits = _rrf_merge(vector_hits, text_hits, k=60)

    candidates_after = len(combined_hits)

    # ── 5. Convert to chunk dicts ─────────────────────────────────────────
    chunk_dicts = [_hit_to_chunk_dict(h) for h in combined_hits]

    # ── 6. Optional reranking ─────────────────────────────────────────────
    reranking_time_ms = 0.0
    if options.use_reranking and chunk_dicts:
        t_rerank_start = time.perf_counter()
        chunk_dicts = await rerank(question, chunk_dicts, top_k=5)
        reranking_time_ms = (time.perf_counter() - t_rerank_start) * 1000

    # ── 7. Build top-5 RetrievedChunk list ────────────────────────────────
    top_chunks = chunk_dicts[:5]
    retrieved = [
        RetrievedChunk(**{**c, "rank": idx + 1})
        for idx, c in enumerate(top_chunks)
    ]

    retrieval_time_ms = (t_retrieval - t_start) * 1000

    # Titan doesn't support contextual embeddings; note it in debug
    embedding_mode_note = options.embedding_mode
    if embedding_mode_note == "contextual":
        emb_corpus = "amazon.titan-embed-text-v1 (contextual: Not available)"
    else:
        emb_corpus = "amazon.titan-embed-text-v1"

    debug = DebugInfo(
        embedding_model_corpus=emb_corpus,
        embedding_model_query="amazon.titan-embed-text-v1",
        filters_applied={"filter_clauses": filter_clauses} if filter_clauses else {},
        hybrid_search_used=hybrid_used,
        reranking_used=options.use_reranking,
        candidates_before_filter=candidates_before,
        candidates_after_filter=candidates_after,
        retrieval_time_ms=round(retrieval_time_ms, 1),
        reranking_time_ms=round(reranking_time_ms, 1),
        llm_time_ms=0.0,  # filled in by the router
        chunks_sent_to_llm=len(top_chunks),
        total_time_ms=0.0,  # filled in by the router
    )

    return retrieved, debug
