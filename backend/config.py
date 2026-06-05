from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # MongoDB Atlas
    mongodb_uri: str = ""
    mongodb_database: str = "mybank"
    mongodb_collection: str = "bank_chunks"

    # Aurora PostgreSQL
    aurora_host: str = ""
    aurora_port: int = 5432
    aurora_database: str = "mybank"
    aurora_user: str = ""
    aurora_password: str = ""
    aurora_cluster_arn: str = ""
    aurora_secret_arn: str = ""

    # OpenSearch Service
    opensearch_host: str = ""
    opensearch_port: int = 443
    opensearch_user: str = "admin"
    opensearch_password: str = ""

    # Voyage AI
    voyage_api_key: str = ""

    # AWS
    aws_region: str = "ap-southeast-1"
    aws_bedrock_embeddings_region: str = "us-east-1"

    # LLM (Claude via Bedrock)
    bedrock_model_id: str = "us.anthropic.claude-sonnet-4-5-v2-20250514"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
