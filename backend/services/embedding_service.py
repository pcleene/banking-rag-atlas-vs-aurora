"""Embedding service supporting Voyage AI (MongoDB path) and Titan via Bedrock (OpenSearch path)."""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Literal

import boto3
import voyageai

from backend.config import get_settings

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Voyage AI embeddings  (used by the MongoDB path)
# ---------------------------------------------------------------------------

_voyage_client: voyageai.Client | None = None


def _get_voyage_client() -> voyageai.Client:
    global _voyage_client
    if _voyage_client is None:
        settings = get_settings()
        _voyage_client = voyageai.Client(api_key=settings.voyage_api_key)
    return _voyage_client


async def embed_query_voyage(
    text: str,
    mode: Literal["contextual", "standard", "shared_space"] = "contextual",
) -> list[float]:
    """Embed a single query string using Voyage AI.

    * contextual / standard -> voyage-context-3 via contextualized_embed
      (corpus is always voyage-context-3, so queries must match)
    * shared_space -> voyage-4-lite via embed()
      (corpus has a separate embedding_v4 field with voyage-4 vectors)
    """
    client = _get_voyage_client()

    if mode == "shared_space":
        def _call_v4() -> list[float]:
            result = client.embed([text], model="voyage-4-lite", input_type="query")
            return result.embeddings[0]

        return await asyncio.to_thread(_call_v4)

    # contextual and standard both query against voyage-context-3 corpus
    def _call() -> list[float]:
        result = client.contextualized_embed(
            inputs=[[text]],
            model="voyage-context-3",
            input_type="query",
        )
        return result.results[0].embeddings[0]

    return await asyncio.to_thread(_call)


async def embed_chunks_voyage(
    chunks: list[dict],
    mode: Literal["contextual", "standard", "shared_space"] = "contextual",
) -> list[list[float]]:
    """Embed document chunks using Voyage AI (for ingestion).

    * contextual   -> voyageai contextualized_embed with voyage-context-3
    * standard     -> voyage-context-3, input_type="document"
    * shared_space -> voyage-4, input_type="document"

    Each element in *chunks* should be a dict with at least a 'content' key.
    For contextual mode, a 'context' key is also expected.
    """
    client = _get_voyage_client()

    if mode == "contextual":

        def _call_contextual() -> list[list[float]]:
            documents = [c["content"] for c in chunks]
            contexts = [c.get("context", "") for c in chunks]
            result = client.contextualized_embed(
                documents=documents,
                contexts=contexts,
                model="voyage-context-3",
                input_type="document",
            )
            return result.embeddings

        return await asyncio.to_thread(_call_contextual)

    elif mode == "shared_space":
        model = "voyage-4"
    else:
        model = "voyage-context-3"

    def _call_standard() -> list[list[float]]:
        texts = [c["content"] for c in chunks]
        result = client.embed(texts, model=model, input_type="document")
        return result.embeddings

    return await asyncio.to_thread(_call_standard)


# ---------------------------------------------------------------------------
# Titan V2 embeddings via Bedrock  (used by the OpenSearch path)
# ---------------------------------------------------------------------------

_bedrock_embeddings_client = None


def _get_bedrock_embeddings_client():
    global _bedrock_embeddings_client
    if _bedrock_embeddings_client is None:
        settings = get_settings()
        _bedrock_embeddings_client = boto3.client(
            "bedrock-runtime",
            region_name=settings.aws_bedrock_embeddings_region,
        )
    return _bedrock_embeddings_client


async def embed_query_titan(text: str) -> list[float]:
    """Embed a single query string using Amazon Titan Embed Text V2 (1536-dim)."""

    def _call() -> list[float]:
        client = _get_bedrock_embeddings_client()
        body = json.dumps({"inputText": text})
        response = client.invoke_model(
            modelId="amazon.titan-embed-text-v1",
            contentType="application/json",
            accept="application/json",
            body=body,
        )
        result = json.loads(response["body"].read())
        return result["embedding"]

    return await asyncio.to_thread(_call)


async def embed_chunks_titan(texts: list[str]) -> list[list[float]]:
    """Batch embed texts using Amazon Titan Embed Text V2 (1536-dim).

    Titan does not natively support batch requests, so we call one-by-one
    inside a thread pool.
    """

    def _call_single(text: str) -> list[float]:
        client = _get_bedrock_embeddings_client()
        body = json.dumps({"inputText": text})
        response = client.invoke_model(
            modelId="amazon.titan-embed-text-v1",
            contentType="application/json",
            accept="application/json",
            body=body,
        )
        result = json.loads(response["body"].read())
        return result["embedding"]

    tasks = [asyncio.to_thread(_call_single, t) for t in texts]
    return await asyncio.gather(*tasks)
