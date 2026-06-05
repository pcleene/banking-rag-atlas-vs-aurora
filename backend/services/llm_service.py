"""LLM service - Claude via AWS Bedrock converse API."""

from __future__ import annotations

import asyncio
import logging
import time

import boto3

from backend.config import get_settings

logger = logging.getLogger(__name__)

_bedrock_client = None


def _get_bedrock_client():
    global _bedrock_client
    if _bedrock_client is None:
        settings = get_settings()
        _bedrock_client = boto3.client(
            "bedrock-runtime",
            region_name=settings.aws_region,
        )
    return _bedrock_client


_PROMPT_TEMPLATE = """\
You are a Malaysian banking assistant for MYBank. Answer the customer's question based ONLY on the provided context. Cite which document(s) you used. If the context contains conflicting information from different time periods, prefer the most recent document marked as 'current'.

Context:
{context}

Question: {question}

Answer:"""


def _build_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into the context block for the prompt."""
    parts: list[str] = []
    for c in chunks:
        header = (
            f"[Source: {c.get('source_title', 'Unknown')}"
            f" | Date: {c.get('source_date', 'N/A')}"
            f" | Status: {c.get('source_status', 'N/A')}"
            f" | Entity: {c.get('source_entity', 'N/A')}]"
        )
        parts.append(f"{header}\n{c.get('content', '')}")
    return "\n\n".join(parts)


async def generate_answer(
    question: str,
    chunks: list[dict],
    backend: str,
) -> tuple[str, float]:
    """Generate an answer using Claude via Bedrock converse API.

    Parameters
    ----------
    question : str
        The user's question.
    chunks : list[dict]
        Retrieved document chunks (must have content and source metadata).
    backend : str
        Which backend was used ("mongodb" or "opensearch") - logged for tracing.

    Returns
    -------
    tuple[str, float]
        (answer_text, llm_time_ms)
    """
    settings = get_settings()
    client = _get_bedrock_client()

    context = _build_context(chunks)
    prompt = _PROMPT_TEMPLATE.format(context=context, question=question)

    def _call() -> str:
        response = client.converse(
            modelId=settings.bedrock_model_id,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}],
                }
            ],
            inferenceConfig={"maxTokens": 1024, "temperature": 0},
        )
        # Extract text from the converse response
        output_message = response.get("output", {}).get("message", {})
        content_blocks = output_message.get("content", [])
        answer_parts = [
            block["text"] for block in content_blocks if "text" in block
        ]
        return "\n".join(answer_parts)

    start = time.perf_counter()
    answer = await asyncio.to_thread(_call)
    llm_time_ms = (time.perf_counter() - start) * 1000

    logger.info(
        "LLM answer generated via %s backend in %.1f ms", backend, llm_time_ms
    )
    return answer, llm_time_ms
