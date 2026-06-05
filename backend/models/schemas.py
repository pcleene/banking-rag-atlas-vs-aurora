"""Pydantic v2 schemas for BankAssist AI API."""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


# ── Request Models ───────────────────────────────────────────────────────────


class QueryFilters(BaseModel):
    status: Optional[str] = None
    entity: Optional[str] = None
    document_type: Optional[str] = None


class QueryOptions(BaseModel):
    use_hybrid_search: bool = False
    use_reranking: bool = False
    embedding_mode: Literal["contextual", "standard", "shared_space"] = "contextual"
    show_debug: bool = False


class QueryRequest(BaseModel):
    question: str
    backend: Literal["mongodb", "opensearch"]
    filters: QueryFilters = Field(default_factory=QueryFilters)
    options: QueryOptions = Field(default_factory=QueryOptions)


# ── Response Models ──────────────────────────────────────────────────────────


class RetrievedChunk(BaseModel):
    content: str
    source_title: str
    source_date: Optional[str] = None
    source_entity: Optional[str] = None
    source_status: Optional[str] = None
    document_type: Optional[str] = None
    section: Optional[str] = None
    fiscal_year: Optional[int] = None
    version: Optional[str] = None
    superseded_by: Optional[str] = None
    people_mentioned: Optional[list[dict]] = None
    product_info: Optional[dict] = None
    score: float
    rank: int


class DebugInfo(BaseModel):
    embedding_model_corpus: str
    embedding_model_query: str
    filters_applied: dict
    hybrid_search_used: bool
    reranking_used: bool
    candidates_before_filter: int
    candidates_after_filter: int
    retrieval_time_ms: float
    reranking_time_ms: float
    llm_time_ms: float
    chunks_sent_to_llm: int
    total_time_ms: float


class QueryResponse(BaseModel):
    answer: str
    backend: str
    retrieved_chunks: list[RetrievedChunk]
    debug: Optional[DebugInfo] = None


# ── Scenario Models ──────────────────────────────────────────────────────────


class Scenario(BaseModel):
    id: int
    title: str
    query: str
    description: str
    expected_correct: str
    expected_failure: str
    suggested_filters: dict = Field(default_factory=dict)
    suggested_options: dict = Field(default_factory=dict)
