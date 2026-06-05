"""MongoDB Atlas Vector Search retrieval service."""

from __future__ import annotations

import logging
import time
from typing import Any

from backend.config import get_settings
from backend.models.schemas import (
    DebugInfo,
    QueryFilters,
    QueryOptions,
    RetrievedChunk,
)
from backend.services.embedding_service import embed_query_voyage
from backend.services.reranking_service import rerank

logger = logging.getLogger(__name__)


def _build_prefilter(filters: QueryFilters) -> dict | None:
    """Build a MongoDB pre-filter dict for $vectorSearch.

    Uses exact-match on keyword fields -- NO regex.
    """
    conditions: list[dict] = []
    if filters.status:
        conditions.append({"source.status": filters.status})
    if filters.entity:
        conditions.append({"source.entity": filters.entity})
    if filters.document_type:
        conditions.append({"source.document_type": filters.document_type})

    if not conditions:
        return None
    if len(conditions) == 1:
        return conditions[0]
    return {"$and": conditions}


def _doc_to_chunk_dict(doc: dict) -> dict:
    """Convert a MongoDB document to a flat dict suitable for RetrievedChunk."""
    source: dict = doc.get("source", {})
    published = source.get("published_date")
    if published and hasattr(published, "isoformat"):
        published = published.isoformat()

    product = doc.get("product")
    product_info = None
    if product:
        product_info = {
            "product_name": product.get("product_name"),
            "product_category": product.get("product_category"),
        }

    return {
        "content": doc.get("content", ""),
        "source_title": source.get("document_title", ""),
        "source_date": str(published) if published else None,
        "source_entity": source.get("entity"),
        "source_status": source.get("status"),
        "document_type": source.get("document_type"),
        "section": source.get("section"),
        "fiscal_year": source.get("fiscal_year"),
        "version": source.get("version"),
        "superseded_by": source.get("superseded_by"),
        "people_mentioned": doc.get("people_mentioned"),
        "product_info": product_info,
        "score": doc.get("vs_score", 0.0),
    }


def _rrf_merge(
    vector_results: list[dict],
    text_results: list[dict],
    k: int = 60,
) -> list[dict]:
    """Reciprocal Rank Fusion of two ranked lists."""
    scores: dict[str, float] = {}
    doc_map: dict[str, dict] = {}

    for rank, doc in enumerate(vector_results):
        doc_id = str(doc.get("_id", rank))
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
        doc_map[doc_id] = doc

    for rank, doc in enumerate(text_results):
        doc_id = str(doc.get("_id", f"text_{rank}"))
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
        if doc_id not in doc_map:
            doc_map[doc_id] = doc

    sorted_ids = sorted(scores, key=lambda x: scores[x], reverse=True)
    merged = []
    for doc_id in sorted_ids:
        doc = doc_map[doc_id].copy()
        doc["vs_score"] = scores[doc_id]
        merged.append(doc)
    return merged


async def query_mongodb(
    question: str,
    filters: QueryFilters,
    options: QueryOptions,
    db_client: Any,
) -> tuple[list[RetrievedChunk], DebugInfo]:
    """Run a vector (+ optional hybrid) search against MongoDB Atlas.

    Parameters
    ----------
    question : str
        Natural language query.
    filters : QueryFilters
        Optional metadata filters.
    options : QueryOptions
        Search options (hybrid, reranking, embedding mode, etc.).
    db_client : AsyncMongoClient
        The pymongo async client stored in app.state.

    Returns
    -------
    tuple[list[RetrievedChunk], DebugInfo]
    """
    settings = get_settings()
    mode = options.embedding_mode
    t_start = time.perf_counter()

    # ── 1. Embed query ────────────────────────────────────────────────────
    query_vector = await embed_query_voyage(question, mode=mode)

    # ── 2. Build pre-filter ───────────────────────────────────────────────
    prefilter = _build_prefilter(filters)

    # ── 3. Run search (vector-only or hybrid via $rankFusion) ────────────
    db = db_client[settings.mongodb_database]
    collection = db[settings.mongodb_collection]

    # Select index and path based on embedding mode
    if mode == "shared_space":
        vs_index = "vector_index_v4"
        vs_path = "embedding_v4"
    else:
        vs_index = "vector_index"
        vs_path = "embedding"

    # Build the vector search sub-pipeline
    vs_stage: dict[str, Any] = {
        "$vectorSearch": {
            "index": vs_index,
            "path": vs_path,
            "queryVector": query_vector,
            "numCandidates": 150,
            "limit": 20,
        }
    }
    if prefilter:
        vs_stage["$vectorSearch"]["filter"] = prefilter

    hybrid_used = False

    if options.use_hybrid_search:
        # ── Native hybrid search via $rankFusion ───────────────────────
        hybrid_used = True
        rank_fusion_pipeline: list[dict] = [
            {
                "$rankFusion": {
                    "input": {
                        "pipelines": {
                            "vector": [vs_stage],
                            "fulltext": [
                                {
                                    "$search": {
                                        "index": "text_index",
                                        "text": {
                                            "query": question,
                                            "path": "content",
                                        },
                                    }
                                },
                                {"$limit": 20},
                            ],
                        }
                    }
                }
            },
            {"$addFields": {"vs_score": {"$meta": "score"}}},
        ]
        # Apply metadata filter after rankFusion (text search doesn't pre-filter)
        if prefilter:
            rank_fusion_pipeline.append({"$match": prefilter})
        rank_fusion_pipeline.append({"$limit": 20})
        pipeline = rank_fusion_pipeline
    else:
        # ── Vector-only search ─────────────────────────────────────────
        pipeline = [
            vs_stage,
            {"$addFields": {"vs_score": {"$meta": "vectorSearchScore"}}},
        ]

    combined: list[dict] = []
    cursor = await collection.aggregate(pipeline)
    async for doc in cursor:
        combined.append(doc)

    candidates_before = len(combined)

    t_retrieval = time.perf_counter()

    candidates_after = len(combined)

    # ── 5. Convert to chunk dicts ─────────────────────────────────────────
    chunk_dicts = [_doc_to_chunk_dict(doc) for doc in combined]

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

    # Determine embedding model names for debug
    if mode == "shared_space":
        emb_corpus = "voyage-4"
        emb_query = "voyage-4-lite"
    else:
        emb_corpus = "voyage-context-3 (contextual)"
        emb_query = "voyage-context-3"

    debug = DebugInfo(
        embedding_model_corpus=emb_corpus,
        embedding_model_query=emb_query,
        filters_applied=prefilter or {},
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
