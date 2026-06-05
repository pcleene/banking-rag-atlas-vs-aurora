"""BankAssist AI -- FastAPI application entry point."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from opensearchpy import OpenSearch
from pymongo import AsyncMongoClient

from backend.config import get_settings
from backend.routers import admin, query, scenarios

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage startup / shutdown of external clients."""
    settings = get_settings()

    # ── MongoDB (pymongo 4.0+ async) ──────────────────────────────────────
    logger.info("Connecting to MongoDB Atlas ...")
    app.state.mongo_client = AsyncMongoClient(settings.mongodb_uri)
    # Verify connectivity (optional but useful at startup)
    try:
        await app.state.mongo_client.admin.command("ping")
        logger.info("MongoDB connection verified.")
    except Exception as exc:
        logger.warning("MongoDB ping failed (will retry on first query): %s", exc)

    # ── OpenSearch ────────────────────────────────────────────────────────
    logger.info("Connecting to OpenSearch ...")
    os_host = settings.opensearch_host
    if os_host.startswith("https://"):
        os_host = os_host[8:]
    elif os_host.startswith("http://"):
        os_host = os_host[7:]
    use_ssl = settings.opensearch_port == 443

    app.state.os_client = OpenSearch(
        hosts=[{"host": os_host, "port": settings.opensearch_port}],
        http_auth=(settings.opensearch_user, settings.opensearch_password),
        use_ssl=use_ssl,
        verify_certs=use_ssl,
        ssl_show_warn=False,
    )
    try:
        info = app.state.os_client.info()
        logger.info(
            "OpenSearch connection verified: %s",
            info.get("version", {}).get("number", "unknown"),
        )
    except Exception as exc:
        logger.warning(
            "OpenSearch info call failed (will retry on first query): %s", exc
        )

    yield

    # ── Shutdown ──────────────────────────────────────────────────────────
    logger.info("Shutting down clients ...")
    await app.state.mongo_client.close()
    app.state.os_client.close()
    logger.info("Clients closed.")


app = FastAPI(
    title="BankAssist AI",
    description="RAG comparison demo: MongoDB Atlas vs OpenSearch",
    version="0.1.0",
    lifespan=lifespan,
)

# ── CORS (allow all for development) ──────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────
app.include_router(query.router, prefix="/api", tags=["Query"])
app.include_router(scenarios.router, prefix="/api", tags=["Scenarios"])
app.include_router(admin.router, prefix="/api", tags=["Admin"])


@app.get("/health")
async def health():
    """Simple health-check endpoint."""
    return {"status": "ok"}
