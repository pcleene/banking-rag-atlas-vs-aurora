"""Load data from Aurora PostgreSQL into OpenSearch with Titan embeddings.

Reads from Aurora via RDS Data API, denormalizes, embeds with Titan via Bedrock
(us-east-1), and bulk indexes into OpenSearch with flat mapping.
"""

import asyncio
import json
import os
import sys
import time

import boto3
from opensearchpy import OpenSearch, helpers

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.config import get_settings

OPENSEARCH_INDEX = "bank_chunks"

INDEX_MAPPING = {
    "settings": {
        "index": {
            "knn": True,
            "knn.algo_param.ef_search": 100,
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }
    },
    "mappings": {
        "properties": {
            "chunk_id": {"type": "integer"},
            "document_id": {"type": "integer"},
            "content": {"type": "text"},
            "embedding": {
                "type": "knn_vector",
                "dimension": 1536,
                "method": {
                    "name": "hnsw",
                    "space_type": "cosinesimil",
                    "engine": "lucene",
                },
            },
            "document_title": {"type": "keyword"},
            "document_type": {"type": "keyword"},
            "entity": {"type": "keyword"},
            "published_date": {"type": "date"},
            "fiscal_year": {"type": "integer"},
            "version": {"type": "keyword"},
            "status": {"type": "keyword"},
            "section": {"type": "keyword"},
            "product_name": {"type": "keyword"},
            "product_category": {"type": "keyword"},
            "person_names": {"type": "keyword"},
            "person_roles": {"type": "keyword"},
            "person_entities": {"type": "keyword"},
            "fee_types": {"type": "keyword"},
            "fee_amounts": {"type": "float"},
            "bnm_circulars": {"type": "keyword"},
            "compliance_categories": {"type": "keyword"},
            "target_audience": {"type": "keyword"},
            "regions": {"type": "keyword"},
            "chunk_index": {"type": "integer"},
            "total_chunks": {"type": "integer"},
        }
    },
}

# Split the denormalization into two queries to avoid complex joins
# that exceed Data API response limits
CHUNKS_QUERY = """
    SELECT
        c.id AS chunk_id,
        c.document_id,
        c.content,
        c.section,
        c.page_range,
        c.chunk_index,
        c.total_chunks,
        d.title AS document_title,
        d.document_type,
        d.entity,
        d.published_date,
        d.fiscal_year,
        d.version,
        d.status
    FROM chunks c
    JOIN documents d ON c.document_id = d.id
    ORDER BY c.id
"""

PEOPLE_QUERY = """
    SELECT chunk_id, person_name, role, entity
    FROM people_mentions
    ORDER BY chunk_id
"""

PRODUCT_QUERY = """
    SELECT document_id, product_name, product_category, fee_schedule
    FROM product_metadata
"""

REGULATORY_QUERY = """
    SELECT document_id, bnm_circulars, compliance_categories
    FROM regulatory_info
"""


def embed_with_titan(texts: list[str], bedrock_client) -> list[list[float]]:
    """Embed texts with Amazon Titan Embeddings v1 via Bedrock (1536 dims)."""
    embeddings = []

    for i, text in enumerate(texts):
        truncated = text[:8000]
        response = bedrock_client.invoke_model(
            modelId="amazon.titan-embed-text-v1",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({"inputText": truncated}),
        )
        result = json.loads(response["body"].read())
        embeddings.append(result["embedding"])

        if (i + 1) % 10 == 0:
            print(f"    Embedded {i + 1}/{len(texts)} chunks...")

    return embeddings


def _extract_cell(cell):
    """Extract value from an RDS Data API cell."""
    if "isNull" in cell and cell["isNull"]:
        return None
    if "longValue" in cell:
        return cell["longValue"]
    if "doubleValue" in cell:
        return cell["doubleValue"]
    if "stringValue" in cell:
        return cell["stringValue"]
    if "booleanValue" in cell:
        return cell["booleanValue"]
    if "arrayValue" in cell:
        arr = cell["arrayValue"]
        if "stringValues" in arr:
            return arr["stringValues"]
        return []
    return None


def data_api_query(rds_data, cluster_arn, secret_arn, database, sql):
    """Execute a query via RDS Data API and return list of dicts."""
    result = rds_data.execute_statement(
        resourceArn=cluster_arn,
        secretArn=secret_arn,
        database=database,
        sql=sql,
        includeResultMetadata=True,
    )
    columns = [col["name"] for col in result["columnMetadata"]]
    rows = []
    for record in result.get("records", []):
        row = {}
        for col_name, cell in zip(columns, record):
            row[col_name] = _extract_cell(cell)
        rows.append(row)
    return rows


def flatten_for_opensearch(row: dict, people_by_chunk, products_by_doc, regulatory_by_doc) -> dict:
    """Denormalize an Aurora row into a flat OpenSearch document."""
    doc = {
        "chunk_id": row["chunk_id"],
        "document_id": row["document_id"],
        "content": row["content"],
        "document_title": row["document_title"],
        "document_type": row["document_type"],
        "entity": row["entity"],
        "published_date": row["published_date"] if row["published_date"] else None,
        "fiscal_year": row["fiscal_year"],
        "version": row["version"],
        "status": row["status"],
        "section": row["section"],
        "chunk_index": row["chunk_index"],
        "total_chunks": row["total_chunks"],
    }

    # Flatten people mentions — LOSES name-to-role association
    people = people_by_chunk.get(row["chunk_id"], [])
    doc["person_names"] = [p["person_name"] for p in people]
    doc["person_roles"] = [p["role"] for p in people]
    doc["person_entities"] = [p.get("entity", "") for p in people]

    # Flatten product metadata — LOSES fee-type-to-amount association
    product = products_by_doc.get(row["document_id"])
    if product:
        doc["product_name"] = product.get("product_name")
        doc["product_category"] = product.get("product_category")
        fee_schedule = product.get("fee_schedule")
        if fee_schedule:
            if isinstance(fee_schedule, str):
                fee_schedule = json.loads(fee_schedule)
            doc["fee_types"] = [f.get("fee_type", "") for f in fee_schedule]
            amounts = []
            for f in fee_schedule:
                val = f.get("amount") or f.get("percentage") or 0
                if isinstance(val, str):
                    # Strip currency prefix like "RM200" -> 200
                    import re
                    nums = re.findall(r"[\d.]+", val)
                    val = float(nums[0]) if nums else 0
                amounts.append(float(val))
            doc["fee_amounts"] = amounts

    # Flatten regulatory
    reg = regulatory_by_doc.get(row["document_id"], {})
    doc["bnm_circulars"] = reg.get("bnm_circulars") or []
    doc["compliance_categories"] = reg.get("compliance_categories") or []

    return doc


async def load_opensearch():
    settings = get_settings()

    if not settings.aurora_cluster_arn:
        print("ERROR: AURORA_CLUSTER_ARN not set in .env (need Aurora Data API)")
        return
    if not settings.opensearch_host:
        print("ERROR: OPENSEARCH_HOST not set in .env")
        return

    print("=" * 60)
    print("Loading data from Aurora into OpenSearch (via Data API)")
    print("=" * 60)

    # Setup Data API client
    rds_data = boto3.client("rds-data", region_name=settings.aws_region)
    cluster_arn = settings.aurora_cluster_arn
    secret_arn = settings.aurora_secret_arn
    database = settings.aurora_database

    # Read from Aurora via Data API
    print("\n[1/4] Reading denormalized data from Aurora (via Data API)...")
    chunk_rows = data_api_query(rds_data, cluster_arn, secret_arn, database, CHUNKS_QUERY)
    print(f"  Read {len(chunk_rows)} chunks")

    people_rows = data_api_query(rds_data, cluster_arn, secret_arn, database, PEOPLE_QUERY)
    print(f"  Read {len(people_rows)} people mentions")

    product_rows = data_api_query(rds_data, cluster_arn, secret_arn, database, PRODUCT_QUERY)
    print(f"  Read {len(product_rows)} product records")

    regulatory_rows = data_api_query(rds_data, cluster_arn, secret_arn, database, REGULATORY_QUERY)
    print(f"  Read {len(regulatory_rows)} regulatory records")

    # Build lookup tables
    people_by_chunk: dict[int, list] = {}
    for p in people_rows:
        people_by_chunk.setdefault(p["chunk_id"], []).append(p)

    products_by_doc = {r["document_id"]: r for r in product_rows}
    regulatory_by_doc = {r["document_id"]: r for r in regulatory_rows}

    # Flatten for OpenSearch
    print("\n[2/4] Flattening documents for OpenSearch (losing field associations)...")
    flat_docs = [
        flatten_for_opensearch(row, people_by_chunk, products_by_doc, regulatory_by_doc)
        for row in chunk_rows
    ]
    print(f"  Flattened {len(flat_docs)} documents")

    # Embed with Titan
    print("\n[3/4] Embedding chunks with Amazon Titan v2 (us-east-1)...")
    bedrock = boto3.client(
        "bedrock-runtime", region_name=settings.aws_bedrock_embeddings_region
    )
    texts = [doc["content"] for doc in flat_docs]
    start = time.time()
    embeddings = embed_with_titan(texts, bedrock)
    embed_time = time.time() - start
    print(f"  Embedded {len(embeddings)} chunks in {embed_time:.1f}s")

    for doc, emb in zip(flat_docs, embeddings):
        doc["embedding"] = emb

    # Index into OpenSearch
    print("\n[4/4] Indexing into OpenSearch...")
    os_host = settings.opensearch_host
    if os_host.startswith("https://"):
        os_host = os_host[8:]
    elif os_host.startswith("http://"):
        os_host = os_host[7:]

    os_client = OpenSearch(
        hosts=[{"host": os_host, "port": settings.opensearch_port}],
        http_auth=(settings.opensearch_user, settings.opensearch_password),
        use_ssl=settings.opensearch_port == 443,
        verify_certs=True,
        ssl_show_warn=False,
    )

    # Delete existing index
    if os_client.indices.exists(index=OPENSEARCH_INDEX):
        os_client.indices.delete(index=OPENSEARCH_INDEX)
        print("  Deleted existing index")

    # Create index with mapping
    os_client.indices.create(index=OPENSEARCH_INDEX, body=INDEX_MAPPING)
    print("  Created index with kNN mapping")

    # Bulk index
    actions = [
        {
            "_index": OPENSEARCH_INDEX,
            "_id": doc["chunk_id"],
            "_source": doc,
        }
        for doc in flat_docs
    ]

    success, errors = helpers.bulk(os_client, actions, raise_on_error=False)
    print(f"  Indexed {success} documents")
    if errors:
        print(f"  Errors: {len(errors)}")
        for err in errors[:3]:
            print(f"    {err}")

    print("\nOpenSearch loading complete!")
    print(f"  Index: {OPENSEARCH_INDEX}")
    print(f"  Documents: {success}")


if __name__ == "__main__":
    asyncio.run(load_opensearch())
