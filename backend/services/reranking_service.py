"""Reranking service using Voyage AI rerank-2 model."""

from __future__ import annotations

import asyncio
import logging

import voyageai

from backend.config import get_settings

logger = logging.getLogger(__name__)

_voyage_client: voyageai.Client | None = None


def _get_voyage_client() -> voyageai.Client:
    global _voyage_client
    if _voyage_client is None:
        settings = get_settings()
        _voyage_client = voyageai.Client(api_key=settings.voyage_api_key)
    return _voyage_client


async def rerank(
    question: str,
    chunks: list[dict],
    top_k: int = 5,
) -> list[dict]:
    """Rerank retrieved chunks using Voyage AI rerank-2.

    Parameters
    ----------
    question : str
        The user query.
    chunks : list[dict]
        Each dict must have at least a ``content`` key.
    top_k : int
        Number of top results to return after reranking.

    Returns
    -------
    list[dict]
        Reordered chunks with an updated ``score`` field reflecting the
        reranker relevance score.
    """
    if not chunks:
        return []

    client = _get_voyage_client()
    documents = [c["content"] for c in chunks]

    def _call():
        return client.rerank(
            query=question,
            documents=documents,
            model="rerank-2",
            top_k=top_k,
        )

    result = await asyncio.to_thread(_call)

    reranked: list[dict] = []
    for item in result.results:
        chunk = chunks[item.index].copy()
        chunk["score"] = item.relevance_score
        reranked.append(chunk)

    return reranked
