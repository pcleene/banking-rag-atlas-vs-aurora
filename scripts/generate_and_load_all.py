"""One-shot script: generate corpus and load all three data stores.

Usage:
    python -m scripts.generate_and_load_all [--mongodb-only] [--aurora-only] [--opensearch-only]

Run from the bankassist-ai/ directory.
"""

import argparse
import asyncio
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def main():
    parser = argparse.ArgumentParser(description="Generate corpus and load all stores")
    parser.add_argument("--mongodb-only", action="store_true", help="Only load MongoDB")
    parser.add_argument("--aurora-only", action="store_true", help="Only load Aurora")
    parser.add_argument(
        "--opensearch-only", action="store_true", help="Only load OpenSearch"
    )
    args = parser.parse_args()

    load_all = not (args.mongodb_only or args.aurora_only or args.opensearch_only)

    if load_all or args.mongodb_only:
        print("\n" + "=" * 60)
        print("STEP 1: Loading MongoDB Atlas")
        print("=" * 60)
        from backend.data.load_mongodb import load_mongodb

        await load_mongodb()

    if load_all or args.aurora_only:
        print("\n" + "=" * 60)
        print("STEP 2: Loading Aurora PostgreSQL")
        print("=" * 60)
        from backend.data.load_aurora import load_aurora

        await load_aurora()

    if load_all or args.opensearch_only:
        print("\n" + "=" * 60)
        print("STEP 3: Loading OpenSearch (from Aurora)")
        print("=" * 60)
        from backend.data.load_opensearch import load_opensearch

        await load_opensearch()

    print("\n" + "=" * 60)
    print("ALL DONE!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
