# BankAssist AI — Changelog

## Project Summary

Side-by-side RAG comparison demo: **MongoDB Atlas** vs **Aurora PostgreSQL + OpenSearch Service**.
Built for Uber Fusion enablement workshop. Fictional bank: MYBank (Malaysian banking context).

---

## Infrastructure Provisioned

| Resource | Engine | Region | Purpose |
|----------|--------|--------|---------|
| MongoDB Atlas (M10) | MongoDB 8.0 | ap-southeast-1 | Vector store + metadata (nested documents) |
| Aurora PostgreSQL Serverless v2 | PostgreSQL 16.6 | ap-southeast-1 | Relational store (7-table schema) |
| OpenSearch Service | OpenSearch 2.x | ap-southeast-1 | Vector store + flat metadata |

## Data Loaded

| Store | Records | Embedding Model | Dimensions |
|-------|---------|-----------------|------------|
| MongoDB Atlas | 77 chunks | voyage-context-3 (contextual) | 1024 |
| Aurora PostgreSQL | 29 docs, 77 chunks, 19 relationships | N/A (relational) | N/A |
| OpenSearch Service | 77 flat documents | Amazon Titan Embed Text v1 | 1536 |

---

## Bugs Found & Fixed

### 1. Aurora Setup — Invalid Parameter
**File:** `scripts/setup_aurora.py`
- **Bug:** `PubliclyAccessible=False` passed to `create_db_cluster`, which is invalid for `aurora-postgresql` engine type
- **Fix:** Removed the parameter

### 2. Voyage Contextual Embedding Response Format
**File:** `backend/data/load_mongodb.py`
- **Bug:** Accessed `result.embeddings[0]` but `contextualized_embed()` returns `result.results[0].embeddings`
- **Fix:** Updated to correct response structure

### 3. Aurora Loader — VPN Blocks Direct TCP
**File:** `backend/data/load_aurora.py`
- **Bug:** Used `asyncpg` for direct PostgreSQL TCP connections, but corporate VPN blocks the Aurora IP range
- **Fix:** Complete rewrite to use AWS RDS Data API via boto3 (HTTP-based, goes through AWS endpoints)
- **Also fixed:** `related_documents` field was being passed as dicts instead of strings

### 4. OpenSearch Loader — Titan v2 Dimension Mismatch
**File:** `backend/data/load_opensearch.py`
- **Bug:** Used Titan Embed Text v2 which caps at 1024 dimensions, but the index mapping was set to 1536
- **Fix:** Switched to Titan Embed Text v1 (native 1536-dim output)
- **Also fixed:** Rewrote to read from Aurora via Data API; fixed `fee_amounts` "RM200" regex parsing for flat mapping

### 5. Query Embedding Model Mismatch
**File:** `backend/services/embedding_service.py`
- **Bug:** Used `voyage-context-3` for query embedding, but that model only works with `contextualized_embed()` (corpus-time API)
- **Fix:** Query model changed to `voyage-3` (same vector space as `voyage-context-3`, works with standard `embed()`)
- **Also fixed:** Titan v2 → v1 for OpenSearch queries to match loader

### 6. MongoDB Service — Async + Pipeline Issues
**File:** `backend/services/mongodb_service.py`
- **Bug 1:** Missing `await` on `aggregate()` — pymongo 4.16+ returns `AsyncCommandCursor` requiring await
- **Bug 2:** Manual RRF implementation was fragile and didn't leverage Atlas Search native capabilities
- **Bug 3:** Metadata filters applied as `$match` before `$rankFusion` caused empty results
- **Fix:** Added `await`; replaced manual RRF with native `$rankFusion` using `$vectorSearch` + `$search` sub-pipelines; moved `$match` to post-filter position after `$rankFusion`

### 7. FastAPI Lifespan — Client Cleanup
**File:** `backend/main.py`
- **Bug:** `AsyncMongoClient.close()` was not `await`ed; OpenSearch host URL included `https://` prefix that the client doesn't expect
- **Fix:** Added `await` to close; strip protocol prefix from OpenSearch host

### 8. Frontend — API Paths + Field Names
**Files:** `frontend/src/lib/api.ts`, `frontend/src/lib/components/ChunkCard.svelte`
- **Bug:** Supersede endpoint path mismatch; field name references assumed nested structure for OpenSearch (which uses flat mapping)
- **Fix:** Corrected API paths; adjusted field accessors for flat vs nested mapping

### 9. Architecture Diagram — Accuracy
**File:** `frontend/src/lib/components/ArchitectureDiagram.svelte`
- **Bug:** MongoDB index shown without dot-notation paths; OpenSearch dimension shown as 1024; reranking labels misleading
- **Fix:** Updated index field paths, corrected dimensions to 1536, clarified reranking as "app-side"

---

## Code Changes by File

### Backend
| File | Changes |
|------|---------|
| `backend/main.py` | FastAPI lifespan with async MongoDB/OpenSearch clients, CORS, health endpoint |
| `backend/config.py` | Pydantic Settings with `.env` loading for all credentials |
| `backend/models/schemas.py` | Request/response models: QueryRequest, QueryResponse, RetrievedChunk, DebugInfo, Scenario |
| `backend/services/embedding_service.py` | Dual embedding: Voyage (voyage-3/context-3) + Titan v1 via Bedrock |
| `backend/services/mongodb_service.py` | Vector search, native $rankFusion hybrid, metadata pre-filter, app-side reranking |
| `backend/services/opensearch_service.py` | kNN search, manual RRF hybrid, flat field filtering, app-side reranking |
| `backend/services/llm_service.py` | Claude Sonnet 4 via Bedrock converse API (ap-southeast-1) |
| `backend/services/reranking_service.py` | Voyage rerank-2, shared by both pipelines |
| `backend/routers/query.py` | POST /api/query — routes to MongoDB or OpenSearch, calls LLM |
| `backend/routers/scenarios.py` | GET /api/scenarios — 8 pre-configured test cases |
| `backend/routers/admin.py` | POST /api/admin/supersede — mark documents as superseded |

### Data Layer
| File | Changes |
|------|---------|
| `backend/data/generate_corpus.py` | Template-based generator: 77 chunks from 29 docs, 250-word chunks |
| `backend/data/templates/annual_report.py` | 8 annual reports (2019-2024 + superseded versions) |
| `backend/data/templates/product_disclosure.py` | 10 product disclosure sheets |
| `backend/data/templates/policy_document.py` | 7 policy documents (with superseded versions) |
| `backend/data/templates/faq.py` | 4 FAQ documents |
| `backend/data/load_mongodb.py` | Corpus → Voyage contextual embedding → MongoDB Atlas |
| `backend/data/load_aurora.py` | Corpus → Aurora PostgreSQL via RDS Data API (7-table schema) |
| `backend/data/load_opensearch.py` | Aurora → flat denormalization → Titan embedding → OpenSearch |

### Frontend
| File | Changes |
|------|---------|
| `frontend/src/routes/+page.svelte` | Main two-column layout with query input + dual pipeline views |
| `frontend/src/routes/+layout.svelte` | Root layout with CSS variables and theme system |
| `frontend/src/lib/api.ts` | TypeScript API client: sendQuery, getScenarios, supersedeDocument |
| `frontend/src/lib/stores/query.ts` | Svelte stores: question, options, results, scenarios |
| `frontend/src/lib/components/QueryInput.svelte` | Query input with scenario dropdown, auto-fills suggested filters |
| `frontend/src/lib/components/PipelineView.svelte` | Per-backend panel: filters, toggles, results, chunks |
| `frontend/src/lib/components/ChunkCard.svelte` | Chunk display with metadata, score, superseded warnings |
| `frontend/src/lib/components/AnswerPanel.svelte` | LLM answer display with streaming feel |
| `frontend/src/lib/components/DebugPanel.svelte` | Timing breakdown chart + retrieval diagnostics |
| `frontend/src/lib/components/FeatureToggle.svelte` | Reusable toggle switch component |
| `frontend/src/lib/components/ArchitectureDiagram.svelte` | Architecture visualization for both pipelines |

### Scripts
| File | Changes |
|------|---------|
| `scripts/setup_aurora.py` | Provision Aurora Serverless v2 cluster |
| `scripts/setup_opensearch.py` | Provision OpenSearch Service domain |
| `scripts/generate_and_load_all.py` | One-shot data loading orchestrator |
