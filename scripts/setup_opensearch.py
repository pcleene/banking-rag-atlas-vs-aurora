"""Provision OpenSearch Service domain in ap-southeast-1.

Creates:
- OpenSearch domain (mybank-search)
- Single t3.medium.search node
- Fine-grained access control with master user
- OpenSearch 2.x

Usage:
    aws sso login
    python scripts/setup_opensearch.py

Outputs connection details to paste into .env
"""

import json
import secrets
import string
import sys
import time

import boto3

REGION = "ap-southeast-1"
DOMAIN_NAME = "mybank-search"
ENGINE_VERSION = "OpenSearch_2.13"
INSTANCE_TYPE = "t3.medium.search"
MASTER_USER = "admin"


def generate_password(length=24):
    """Generate a password meeting OpenSearch requirements."""
    # Must have uppercase, lowercase, digit, and special char
    password = (
        secrets.choice(string.ascii_uppercase)
        + secrets.choice(string.ascii_lowercase)
        + secrets.choice(string.digits)
        + secrets.choice("!@#$%^&*")
    )
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password += "".join(secrets.choice(alphabet) for _ in range(length - 4))
    # Shuffle
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)


def main():
    print("=" * 60)
    print("Provisioning OpenSearch Service Domain")
    print(f"Region: {REGION}")
    print("=" * 60)

    os_client = boto3.client("opensearch", region_name=REGION)

    # Check if domain already exists
    try:
        existing = os_client.describe_domain(DomainName=DOMAIN_NAME)
        endpoint = existing["DomainStatus"].get("Endpoint")
        if endpoint:
            print(f"\nDomain already exists!")
            print(f"  Endpoint: https://{endpoint}")
            print(f"\nAdd to .env:")
            print(f"  OPENSEARCH_HOST=https://{endpoint}")
            print(f"  OPENSEARCH_USER={MASTER_USER}")
            print(f"  OPENSEARCH_PASSWORD=<your-password>")
            return
        else:
            print(f"\nDomain exists but is still being created...")
    except os_client.exceptions.ResourceNotFoundException:
        pass

    password = generate_password()
    print(f"\n[1/2] Generated credentials")
    print(f"  User: {MASTER_USER}")
    print(f"  Password: {password}")

    # Get AWS account ID for access policy
    sts = boto3.client("sts", region_name=REGION)
    account_id = sts.get_caller_identity()["Account"]

    # Create domain
    print("\n[2/2] Creating OpenSearch domain...")
    access_policy = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": "es:*",
                    "Resource": f"arn:aws:es:{REGION}:{account_id}:domain/{DOMAIN_NAME}/*",
                }
            ],
        }
    )

    os_client.create_domain(
        DomainName=DOMAIN_NAME,
        EngineVersion=ENGINE_VERSION,
        ClusterConfig={
            "InstanceType": INSTANCE_TYPE,
            "InstanceCount": 1,
            "DedicatedMasterEnabled": False,
            "ZoneAwarenessEnabled": False,
        },
        EBSOptions={
            "EBSEnabled": True,
            "VolumeType": "gp3",
            "VolumeSize": 20,
        },
        AccessPolicies=access_policy,
        EncryptionAtRestOptions={"Enabled": True},
        NodeToNodeEncryptionOptions={"Enabled": True},
        DomainEndpointOptions={
            "EnforceHTTPS": True,
            "TLSSecurityPolicy": "Policy-Min-TLS-1-2-2019-07",
        },
        AdvancedSecurityOptions={
            "Enabled": True,
            "InternalUserDatabaseEnabled": True,
            "MasterUserOptions": {
                "MasterUserName": MASTER_USER,
                "MasterUserPassword": password,
            },
        },
    )
    print(f"  Domain {DOMAIN_NAME} creation initiated")

    # Wait for domain
    print("\nWaiting for domain to become active (this takes 15-20 minutes)...")
    while True:
        time.sleep(60)
        try:
            status = os_client.describe_domain(DomainName=DOMAIN_NAME)
            processing = status["DomainStatus"].get("Processing", True)
            endpoint = status["DomainStatus"].get("Endpoint")

            if not processing and endpoint:
                break
            print("  Still creating...")
        except Exception as e:
            print(f"  Waiting... ({e})")

    endpoint = status["DomainStatus"]["Endpoint"]

    print("\n" + "=" * 60)
    print("OpenSearch Service domain is ready!")
    print("=" * 60)
    print(f"\nEndpoint: https://{endpoint}")
    print(f"User: {MASTER_USER}")
    print(f"Password: {password}")
    print(f"\nAdd to .env:")
    print(f"  OPENSEARCH_HOST=https://{endpoint}")
    print(f"  OPENSEARCH_PORT=443")
    print(f"  OPENSEARCH_USER={MASTER_USER}")
    print(f"  OPENSEARCH_PASSWORD={password}")


if __name__ == "__main__":
    main()
