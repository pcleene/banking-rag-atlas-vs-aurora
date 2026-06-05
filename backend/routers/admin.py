"""Admin endpoints for BankAssist AI."""

from __future__ import annotations

import logging

from fastapi import APIRouter, Request
from pydantic import BaseModel

from backend.config import get_settings

logger = logging.getLogger(__name__)

router = APIRouter()


class SupersedeRequest(BaseModel):
    document_title: str
    new_status: str = "superseded"


class SupersedeResponse(BaseModel):
    matched_count: int
    modified_count: int
    message: str


@router.post("/admin/supersede", response_model=SupersedeResponse)
async def supersede_document(body: SupersedeRequest, request: Request):
    """Mark all chunks of a given document as superseded in MongoDB.

    Note: On the OpenSearch side the update path is different --
    update Aurora -> wait for CDC replication -> verify sync.
    This endpoint only modifies MongoDB directly.
    """
    settings = get_settings()
    db_client = request.app.state.mongo_client
    db = db_client[settings.mongodb_database]
    collection = db[settings.mongodb_collection]

    result = await collection.update_many(
        {"source.document_title": body.document_title},
        {"$set": {"source.status": body.new_status}},
    )

    message = (
        f"MongoDB: Updated {result.modified_count} chunk(s) for "
        f"'{body.document_title}' to status='{body.new_status}'. "
        f"OpenSearch note: To propagate this change on the OpenSearch side, "
        f"update the source record in Aurora PostgreSQL and wait for CDC "
        f"(Change Data Capture) to sync the change to OpenSearch."
    )

    logger.info(message)

    return SupersedeResponse(
        matched_count=result.matched_count,
        modified_count=result.modified_count,
        message=message,
    )
