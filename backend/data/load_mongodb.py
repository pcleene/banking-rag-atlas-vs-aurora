"""Load chunked corpus into MongoDB Atlas with voyage-context-3 embeddings."""

import asyncio
import os
import sys
import time
from datetime import datetime

import voyageai
from pymongo import AsyncMongoClient

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.config import get_settings
from backend.data.generate_corpus import generate_all_chunks


async def embed_chunks_contextual(
    voyage_client: voyageai.Client, chunks: list[dict]
) -> list[dict]:
    """Embed chunks using voyage-context-3 contextual embeddings.

    Groups chunks by document and uses contextualized_embed to capture
    document-level context in each chunk's vector.
    """
    # Group chunks by document title
    doc_groups: dict[str, list[dict]] = {}
    for chunk in chunks:
        title = chunk["source"]["document_title"]
        doc_groups.setdefault(title, []).append(chunk)

    all_embedded = []
    for title, doc_chunks in doc_groups.items():
        # Sort by chunk_index to maintain order
        doc_chunks.sort(key=lambda c: c["chunk_index"])
        texts = [c["content"] for c in doc_chunks]

        print(f"  Embedding {len(texts)} chunks from: {title}")

        # contextualized_embed takes list of document chunk groups
        # Each group is a list of strings (chunks from one document)
        result = voyage_client.contextualized_embed(
            inputs=[texts],
            model="voyage-context-3",
            input_type="document",
        )

        for chunk, vector in zip(doc_chunks, result.results[0].embeddings):
            chunk["embedding"] = vector
            all_embedded.append(chunk)

    return all_embedded


async def embed_chunks_v4(
    voyage_client: voyageai.Client, chunks: list[dict], batch_size: int = 20
) -> list[dict]:
    """Add voyage-4 embeddings to chunks (stored in 'embedding_v4' field).

    Uses the standard embed() API with voyage-4, input_type="document".
    This provides the 'shared_space' comparison: voyage-4 corpus + voyage-4-lite queries.
    """
    texts = [c["content"] for c in chunks]
    all_embeddings: list[list[float]] = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        print(f"  voyage-4 batch {i // batch_size + 1}/{(len(texts) - 1) // batch_size + 1} ({len(batch)} chunks)")

        def _embed(b=batch):
            return voyage_client.embed(b, model="voyage-4", input_type="document")

        result = await asyncio.to_thread(_embed)
        all_embeddings.extend(result.embeddings)

    for chunk, vec in zip(chunks, all_embeddings):
        chunk["embedding_v4"] = vec

    return chunks


def convert_dates(obj):
    """Recursively convert datetime objects for MongoDB."""
    if isinstance(obj, datetime):
        return obj
    if isinstance(obj, dict):
        return {k: convert_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_dates(item) for item in obj]
    return obj


async def create_vector_search_index(collection):
    """Create the vector search index on the bank_chunks collection."""
    index_definition = {
        "fields": [
            {
                "type": "vector",
                "path": "embedding",
                "numDimensions": 1024,
                "similarity": "cosine",
            },
            {"type": "filter", "path": "source.status"},
            {"type": "filter", "path": "source.document_type"},
            {"type": "filter", "path": "source.entity"},
            {"type": "filter", "path": "source.fiscal_year"},
            {"type": "filter", "path": "source.published_date"},
            {"type": "filter", "path": "product.product_name"},
            {"type": "filter", "path": "people_mentioned.role"},
        ]
    }

    try:
        await collection.create_search_index(
            model={
                "name": "vector_index",
                "type": "vectorSearch",
                "definition": index_definition,
            }
        )
        print("  Created vector search index: vector_index")
    except Exception as e:
        if "already exists" in str(e).lower():
            print("  Vector search index already exists, skipping")
        else:
            print(f"  Warning creating vector search index: {e}")
            print("  You may need to create it manually in the Atlas UI")


async def create_v4_vector_search_index(collection):
    """Create a second vector search index for voyage-4 embeddings (shared_space mode)."""
    index_definition = {
        "fields": [
            {
                "type": "vector",
                "path": "embedding_v4",
                "numDimensions": 1024,
                "similarity": "cosine",
            },
            {"type": "filter", "path": "source.status"},
            {"type": "filter", "path": "source.document_type"},
            {"type": "filter", "path": "source.entity"},
            {"type": "filter", "path": "source.fiscal_year"},
        ]
    }

    try:
        await collection.create_search_index(
            model={
                "name": "vector_index_v4",
                "type": "vectorSearch",
                "definition": index_definition,
            }
        )
        print("  Created vector search index: vector_index_v4")
    except Exception as e:
        if "already exists" in str(e).lower():
            print("  Vector search index vector_index_v4 already exists, skipping")
        else:
            print(f"  Warning creating vector_index_v4: {e}")


async def create_text_search_index(collection):
    """Create Atlas Search index for hybrid search."""
    index_definition = {
        "mappings": {
            "dynamic": False,
            "fields": {
                "content": {"type": "string", "analyzer": "lucene.standard"},
            },
        }
    }

    try:
        await collection.create_search_index(
            model={
                "name": "text_index",
                "type": "search",
                "definition": index_definition,
            }
        )
        print("  Created text search index: text_index")
    except Exception as e:
        if "already exists" in str(e).lower():
            print("  Text search index already exists, skipping")
        else:
            print(f"  Warning creating text search index: {e}")
            print("  You may need to create it manually in the Atlas UI")


async def load_mongodb():
    settings = get_settings()

    if not settings.mongodb_uri:
        print("ERROR: MONGODB_URI not set in .env")
        return

    if not settings.voyage_api_key:
        print("ERROR: VOYAGE_API_KEY not set in .env")
        return

    print("=" * 60)
    print("Loading data into MongoDB Atlas")
    print("=" * 60)

    # Generate corpus
    print("\n[1/5] Generating corpus...")
    chunks = generate_all_chunks()
    print(f"  Generated {len(chunks)} chunks")

    # Embed with voyage-context-3 (contextual) + voyage-4 (shared_space)
    voyage_client = voyageai.Client(api_key=settings.voyage_api_key)

    print("\n[2/6] Embedding chunks with voyage-context-3 (contextual)...")
    start = time.time()
    chunks = await embed_chunks_contextual(voyage_client, chunks)
    embed_time = time.time() - start
    print(f"  Embedded {len(chunks)} chunks in {embed_time:.1f}s")

    print("\n[3/6] Embedding chunks with voyage-4 (shared_space)...")
    start = time.time()
    chunks = await embed_chunks_v4(voyage_client, chunks)
    embed_v4_time = time.time() - start
    print(f"  Embedded {len(chunks)} chunks in {embed_v4_time:.1f}s")

    # Connect to MongoDB
    print("\n[4/6] Connecting to MongoDB Atlas...")
    client = AsyncMongoClient(settings.mongodb_uri)
    db = client[settings.mongodb_database]
    collection = db[settings.mongodb_collection]

    # Clear existing data
    delete_result = await collection.delete_many({})
    print(f"  Cleared {delete_result.deleted_count} existing documents")

    # Insert chunks
    print("\n[5/6] Inserting chunks...")
    docs = [convert_dates(chunk) for chunk in chunks]
    for doc in docs:
        doc["ingested_at"] = datetime.utcnow()

    result = await collection.insert_many(docs)
    print(f"  Inserted {len(result.inserted_ids)} documents")

    # Create indexes
    print("\n[6/6] Creating search indexes...")
    await create_vector_search_index(collection)
    await create_v4_vector_search_index(collection)
    await create_text_search_index(collection)

    await client.close()
    print("\nMongoDB loading complete!")
    print(f"  Collection: {settings.mongodb_database}.{settings.mongodb_collection}")
    print(f"  Documents: {len(chunks)}")
    print(
        "  Note: Search indexes may take a few minutes to become active in Atlas"
    )


if __name__ == "__main__":
    asyncio.run(load_mongodb())
