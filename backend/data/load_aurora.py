"""Load chunked corpus into Aurora PostgreSQL (7-table pragmatic schema).

Uses RDS Data API (boto3) to avoid direct TCP connection issues with VPN.
"""

import asyncio
import json
import os
import sys
from datetime import datetime

import boto3

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.config import get_settings
from backend.data.generate_corpus import generate_all_chunks

DROP_SQL = """
DROP TABLE IF EXISTS regulatory_info CASCADE;
DROP TABLE IF EXISTS product_metadata CASCADE;
DROP TABLE IF EXISTS people_mentions CASCADE;
DROP TABLE IF EXISTS approvals CASCADE;
DROP TABLE IF EXISTS document_relationships CASCADE;
DROP TABLE IF EXISTS chunks CASCADE;
DROP TABLE IF EXISTS documents CASCADE;
"""

SCHEMA_STATEMENTS = [
    """CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        title VARCHAR(500) NOT NULL,
        document_type VARCHAR(50) NOT NULL,
        entity VARCHAR(100) NOT NULL,
        published_date DATE,
        fiscal_year INTEGER,
        version VARCHAR(50),
        status VARCHAR(20) DEFAULT 'current',
        superseded_by_id INTEGER REFERENCES documents(id),
        language VARCHAR(10) DEFAULT 'en',
        data_classification VARCHAR(20) DEFAULT 'public',
        created_at TIMESTAMP DEFAULT NOW(),
        updated_at TIMESTAMP DEFAULT NOW()
    )""",
    """CREATE TABLE IF NOT EXISTS chunks (
        id SERIAL PRIMARY KEY,
        document_id INTEGER REFERENCES documents(id),
        content TEXT NOT NULL,
        section VARCHAR(200),
        page_range VARCHAR(50),
        chunk_index INTEGER,
        total_chunks INTEGER,
        created_at TIMESTAMP DEFAULT NOW()
    )""",
    """CREATE TABLE IF NOT EXISTS document_relationships (
        id SERIAL PRIMARY KEY,
        source_document_id INTEGER REFERENCES documents(id),
        related_document_id INTEGER REFERENCES documents(id),
        relationship_type VARCHAR(50) NOT NULL
    )""",
    """CREATE TABLE IF NOT EXISTS approvals (
        id SERIAL PRIMARY KEY,
        document_id INTEGER REFERENCES documents(id),
        approver_name VARCHAR(200) NOT NULL,
        approver_role VARCHAR(200) NOT NULL,
        approval_date DATE NOT NULL,
        approval_status VARCHAR(20) DEFAULT 'approved',
        sequence_order INTEGER NOT NULL
    )""",
    """CREATE TABLE IF NOT EXISTS people_mentions (
        id SERIAL PRIMARY KEY,
        chunk_id INTEGER REFERENCES chunks(id),
        person_name VARCHAR(200) NOT NULL,
        role VARCHAR(200) NOT NULL,
        entity VARCHAR(100),
        tenure_start DATE,
        tenure_end DATE,
        as_of_date DATE
    )""",
    """CREATE TABLE IF NOT EXISTS product_metadata (
        id SERIAL PRIMARY KEY,
        document_id INTEGER REFERENCES documents(id),
        product_name VARCHAR(200),
        product_category VARCHAR(100),
        effective_date DATE,
        fee_schedule JSONB,
        eligibility_criteria JSONB,
        interest_rates JSONB,
        rewards JSONB
    )""",
    """CREATE TABLE IF NOT EXISTS regulatory_info (
        id SERIAL PRIMARY KEY,
        document_id INTEGER REFERENCES documents(id),
        bnm_circulars TEXT[],
        compliance_categories TEXT[],
        last_review_date DATE,
        reviewer_name VARCHAR(200)
    )""",
]


def to_date_str(dt):
    """Convert datetime to ISO date string or return None."""
    if dt is None:
        return None
    if isinstance(dt, datetime):
        return dt.strftime("%Y-%m-%d")
    if isinstance(dt, str):
        return dt
    return str(dt)


def sql_param(name, value, type_hint="stringValue"):
    """Build an RDS Data API parameter."""
    param = {"name": name}
    if value is None:
        param["value"] = {"isNull": True}
    elif type_hint == "longValue":
        param["value"] = {"longValue": int(value)}
    elif type_hint == "doubleValue":
        param["value"] = {"doubleValue": float(value)}
    elif type_hint == "booleanValue":
        param["value"] = {"booleanValue": bool(value)}
    else:
        param["value"] = {"stringValue": str(value)}
    return param


class DataApiClient:
    """Wrapper around boto3 rds-data for easier SQL execution."""

    def __init__(self, cluster_arn, secret_arn, database, region):
        self.client = boto3.client("rds-data", region_name=region)
        self.cluster_arn = cluster_arn
        self.secret_arn = secret_arn
        self.database = database

    def execute(self, sql, parameters=None):
        kwargs = {
            "resourceArn": self.cluster_arn,
            "secretArn": self.secret_arn,
            "database": self.database,
            "sql": sql,
        }
        if parameters:
            kwargs["parameters"] = parameters
        return self.client.execute_statement(**kwargs)

    def execute_returning_id(self, sql, parameters=None):
        """Execute INSERT ... RETURNING id and return the id."""
        result = self.execute(sql, parameters)
        return result["records"][0][0]["longValue"]

    def fetch_all(self, sql, parameters=None):
        """Execute SELECT and return records with column metadata."""
        kwargs = {
            "resourceArn": self.cluster_arn,
            "secretArn": self.secret_arn,
            "database": self.database,
            "sql": sql,
            "includeResultMetadata": True,
        }
        if parameters:
            kwargs["parameters"] = parameters
        result = self.client.execute_statement(**kwargs)
        columns = [col["name"] for col in result["columnMetadata"]]
        rows = []
        for record in result.get("records", []):
            row = {}
            for col_name, cell in zip(columns, record):
                if "isNull" in cell and cell["isNull"]:
                    row[col_name] = None
                elif "longValue" in cell:
                    row[col_name] = cell["longValue"]
                elif "doubleValue" in cell:
                    row[col_name] = cell["doubleValue"]
                elif "stringValue" in cell:
                    row[col_name] = cell["stringValue"]
                elif "booleanValue" in cell:
                    row[col_name] = cell["booleanValue"]
                elif "arrayValue" in cell:
                    arr = cell["arrayValue"]
                    if "stringValues" in arr:
                        row[col_name] = arr["stringValues"]
                    else:
                        row[col_name] = []
                else:
                    row[col_name] = None
            rows.append(row)
        return rows


async def load_aurora():
    settings = get_settings()

    if not settings.aurora_cluster_arn or not settings.aurora_secret_arn:
        print("ERROR: AURORA_CLUSTER_ARN and AURORA_SECRET_ARN must be set in .env")
        return

    print("=" * 60)
    print("Loading data into Aurora PostgreSQL (via Data API)")
    print("=" * 60)

    # Generate corpus
    print("\n[1/5] Generating corpus...")
    chunks = generate_all_chunks()
    print(f"  Generated {len(chunks)} chunks")

    # Connect via Data API
    print("\n[2/5] Connecting via RDS Data API...")
    db = DataApiClient(
        cluster_arn=settings.aurora_cluster_arn,
        secret_arn=settings.aurora_secret_arn,
        database=settings.aurora_database,
        region=settings.aws_region,
    )
    # Test connection
    result = db.execute("SELECT 1")
    print("  Connected via Data API")

    # Create schema
    print("\n[3/5] Creating schema (7 tables)...")
    # Drop existing tables
    for stmt in DROP_SQL.strip().split(";"):
        stmt = stmt.strip()
        if stmt:
            db.execute(stmt)

    # Create tables
    for stmt in SCHEMA_STATEMENTS:
        db.execute(stmt)
    print("  Created 7 tables")

    # Group chunks by document
    print("\n[4/5] Inserting documents and chunks...")
    doc_groups: dict[str, list[dict]] = {}
    for chunk in chunks:
        title = chunk["source"]["document_title"]
        doc_groups.setdefault(title, []).append(chunk)

    doc_id_map: dict[str, int] = {}  # title -> document id

    for title, doc_chunks in doc_groups.items():
        first = doc_chunks[0]
        src = first["source"]

        # Insert document
        params = [
            sql_param("title", src["document_title"]),
            sql_param("doc_type", src["document_type"]),
            sql_param("entity", src["entity"]),
            sql_param("pub_date", to_date_str(src.get("published_date"))),
            sql_param("fiscal_year", src.get("fiscal_year"),
                      "longValue" if src.get("fiscal_year") is not None else "stringValue"),
            sql_param("version", src.get("version")),
            sql_param("status", src.get("status", "current")),
            sql_param("language", src.get("language", "en")),
            sql_param("data_class", first.get("regulatory", {}).get("data_classification", "public")),
        ]

        doc_id = db.execute_returning_id(
            """INSERT INTO documents (title, document_type, entity, published_date,
                                     fiscal_year, version, status, language, data_classification)
               VALUES (:title, :doc_type, :entity,
                       CAST(:pub_date AS DATE), CAST(:fiscal_year AS INTEGER),
                       :version, :status, :language, :data_class)
               RETURNING id""",
            params,
        )
        doc_id_map[title] = doc_id

        # Insert chunks
        for chunk in doc_chunks:
            chunk_params = [
                sql_param("doc_id", doc_id, "longValue"),
                sql_param("content", chunk["content"]),
                sql_param("section", chunk["source"].get("section")),
                sql_param("page_range", chunk["source"].get("page_range")),
                sql_param("chunk_idx", chunk["chunk_index"], "longValue"),
                sql_param("total", chunk["total_chunks"], "longValue"),
            ]

            chunk_id = db.execute_returning_id(
                """INSERT INTO chunks (document_id, content, section, page_range,
                                      chunk_index, total_chunks)
                   VALUES (:doc_id, :content, :section, :page_range, :chunk_idx, :total)
                   RETURNING id""",
                chunk_params,
            )

            # Insert people mentions
            for person in chunk.get("people_mentioned", []):
                person_params = [
                    sql_param("chunk_id", chunk_id, "longValue"),
                    sql_param("name", person["name"]),
                    sql_param("role", person["role"]),
                    sql_param("entity", person.get("entity")),
                    sql_param("tenure_start", to_date_str(person.get("tenure_start"))),
                    sql_param("tenure_end", to_date_str(person.get("tenure_end"))),
                    sql_param("as_of", to_date_str(src.get("published_date"))),
                ]
                db.execute(
                    """INSERT INTO people_mentions (chunk_id, person_name, role, entity,
                                                    tenure_start, tenure_end, as_of_date)
                       VALUES (:chunk_id, :name, :role, :entity,
                               CAST(:tenure_start AS DATE), CAST(:tenure_end AS DATE),
                               CAST(:as_of AS DATE))""",
                    person_params,
                )

        # Insert approvals
        for i, approval in enumerate(first.get("approvals", [])):
            approval_params = [
                sql_param("doc_id", doc_id, "longValue"),
                sql_param("name", approval["approver"]),
                sql_param("role", approval["role"]),
                sql_param("date", to_date_str(approval["date"])),
                sql_param("status", approval.get("status", "approved")),
                sql_param("seq", i + 1, "longValue"),
            ]
            db.execute(
                """INSERT INTO approvals (document_id, approver_name, approver_role,
                                          approval_date, approval_status, sequence_order)
                   VALUES (:doc_id, :name, :role, CAST(:date AS DATE), :status, :seq)""",
                approval_params,
            )

        # Insert product metadata
        product = first.get("product")
        if product:
            prod_params = [
                sql_param("doc_id", doc_id, "longValue"),
                sql_param("prod_name", product.get("product_name")),
                sql_param("prod_cat", product.get("product_category")),
                sql_param("eff_date", to_date_str(product.get("effective_date"))),
                sql_param("fees", json.dumps(product.get("fee_schedule", []))),
                sql_param("elig", json.dumps(product.get("eligibility_criteria", []))),
                sql_param("rates", json.dumps(product.get("interest_rates", []))),
                sql_param("rewards", json.dumps(product.get("rewards", []))),
            ]
            db.execute(
                """INSERT INTO product_metadata (document_id, product_name, product_category,
                                                 effective_date, fee_schedule, eligibility_criteria,
                                                 interest_rates, rewards)
                   VALUES (:doc_id, :prod_name, :prod_cat, CAST(:eff_date AS DATE),
                           CAST(:fees AS JSONB), CAST(:elig AS JSONB),
                           CAST(:rates AS JSONB), CAST(:rewards AS JSONB))""",
                prod_params,
            )

        # Insert regulatory info
        reg = first.get("regulatory", {})
        if reg:
            circulars = reg.get("bnm_circulars", [])
            categories = reg.get("compliance_categories", [])
            # Data API doesn't natively support TEXT[] — use array constructor
            circulars_str = "ARRAY[" + ",".join(f"'{c}'" for c in circulars) + "]::TEXT[]" if circulars else "ARRAY[]::TEXT[]"
            categories_str = "ARRAY[" + ",".join(f"'{c}'" for c in categories) + "]::TEXT[]" if categories else "ARRAY[]::TEXT[]"
            db.execute(
                f"""INSERT INTO regulatory_info (document_id, bnm_circulars, compliance_categories)
                    VALUES (:doc_id, {circulars_str}, {categories_str})""",
                [sql_param("doc_id", doc_id, "longValue")],
            )

    print(f"  Inserted {len(doc_groups)} documents with {len(chunks)} chunks")

    # Set superseded_by references
    print("\n[5/5] Setting document relationships...")
    relationship_count = 0
    for title, doc_chunks in doc_groups.items():
        first = doc_chunks[0]
        lineage = first.get("lineage", {})

        superseded_by = first["source"].get("superseded_by")
        if superseded_by and superseded_by in doc_id_map:
            db.execute(
                "UPDATE documents SET superseded_by_id = :sup_id WHERE id = :doc_id",
                [
                    sql_param("sup_id", doc_id_map[superseded_by], "longValue"),
                    sql_param("doc_id", doc_id_map[title], "longValue"),
                ],
            )

        for rel in lineage.get("related_documents", []):
            # related_documents can be strings (just titles) or dicts with title/relationship
            if isinstance(rel, str):
                rel_title = rel
                rel_type = "related"
            else:
                rel_title = rel.get("title", rel)
                rel_type = rel.get("relationship", "related")
            if rel_title in doc_id_map:
                db.execute(
                    """INSERT INTO document_relationships
                        (source_document_id, related_document_id, relationship_type)
                       VALUES (:src_id, :rel_id, :rel_type)""",
                    [
                        sql_param("src_id", doc_id_map[title], "longValue"),
                        sql_param("rel_id", doc_id_map[rel_title], "longValue"),
                        sql_param("rel_type", rel_type),
                    ],
                )
                relationship_count += 1

    print(f"  Created {relationship_count} document relationships")

    print("\nAurora PostgreSQL loading complete!")
    print(f"  Database: {settings.aurora_database}")
    print(f"  Documents: {len(doc_groups)}")
    print(f"  Chunks: {len(chunks)}")


if __name__ == "__main__":
    asyncio.run(load_aurora())
