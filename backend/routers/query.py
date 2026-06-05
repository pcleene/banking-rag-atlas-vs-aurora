"""POST /api/query -- main query endpoint."""

from __future__ import annotations

import logging
import time

from fastapi import APIRouter, Request

from backend.models.schemas import QueryRequest, QueryResponse
from backend.services.llm_service import generate_answer
from backend.services.mongodb_service import query_mongodb
from backend.services.opensearch_service import query_opensearch

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def handle_query(body: QueryRequest, request: Request):
    """Route the query to the appropriate backend, call the LLM, and return a
    unified response."""
    t_total_start = time.perf_counter()

    try:
        if body.backend == "mongodb":
            db_client = request.app.state.mongo_client
            retrieved, debug = await query_mongodb(
                question=body.question,
                filters=body.filters,
                options=body.options,
                db_client=db_client,
            )
        else:
            os_client = request.app.state.os_client
            retrieved, debug = await query_opensearch(
                question=body.question,
                filters=body.filters,
                options=body.options,
                os_client=os_client,
            )
    except Exception as exc:
        logger.exception("Retrieval failed for backend=%s", body.backend)
        return QueryResponse(
            answer=f"Retrieval error ({body.backend}): {exc}",
            backend=body.backend,
            retrieved_chunks=[],
            debug=None,
        )

    # ── Call LLM ──────────────────────────────────────────────────────────
    try:
        # Prepare chunk dicts for the LLM prompt
        chunk_dicts = [c.model_dump() for c in retrieved]
        answer, llm_time_ms = await generate_answer(
            question=body.question,
            chunks=chunk_dicts,
            backend=body.backend,
        )
    except Exception as exc:
        logger.exception("LLM call failed")
        answer = f"LLM error: {exc}"
        llm_time_ms = 0.0

    # ── Finalize debug info ───────────────────────────────────────────────
    total_time_ms = (time.perf_counter() - t_total_start) * 1000

    if debug is not None:
        debug.llm_time_ms = round(llm_time_ms, 1)
        debug.total_time_ms = round(total_time_ms, 1)

    return QueryResponse(
        answer=answer,
        backend=body.backend,
        retrieved_chunks=retrieved,
        debug=debug if body.options.show_debug else None,
    )
