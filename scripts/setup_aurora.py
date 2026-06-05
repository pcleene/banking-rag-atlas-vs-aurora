"""Provision Aurora PostgreSQL Serverless v2 in ap-southeast-1.

Creates:
- DB subnet group (uses default VPC subnets)
- Aurora Serverless v2 cluster (mybank-aurora)
- Single db.serverless instance
- Database: mybank

Usage:
    aws sso login
    python scripts/setup_aurora.py

Outputs connection details to paste into .env
"""

import json
import secrets
import string
import sys
import time

import boto3

REGION = "ap-southeast-1"
CLUSTER_ID = "mybank-aurora"
INSTANCE_ID = "mybank-aurora-instance-1"
DB_NAME = "mybank"
DB_USER = "mybankadmin"
SUBNET_GROUP = "mybank-aurora-subnet-group"
ENGINE = "aurora-postgresql"
ENGINE_VERSION = "16.4"
MIN_ACU = 0.5
MAX_ACU = 2.0


def generate_password(length=24):
    """Generate a random password (no special chars that break connection strings)."""
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def get_default_vpc_subnets(ec2):
    """Get subnets from the default VPC."""
    vpcs = ec2.describe_vpcs(Filters=[{"Name": "isDefault", "Values": ["true"]}])
    if not vpcs["Vpcs"]:
        print("ERROR: No default VPC found. Create one or specify subnet IDs manually.")
        sys.exit(1)

    vpc_id = vpcs["Vpcs"][0]["VpcId"]
    subnets = ec2.describe_subnets(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])
    subnet_ids = [s["SubnetId"] for s in subnets["Subnets"]]
    print(f"  Default VPC: {vpc_id}")
    print(f"  Subnets: {subnet_ids}")
    return vpc_id, subnet_ids


def get_or_create_security_group(ec2, vpc_id):
    """Get or create a security group that allows PostgreSQL access."""
    sg_name = "mybank-aurora-sg"

    # Check if it already exists
    sgs = ec2.describe_security_groups(
        Filters=[
            {"Name": "group-name", "Values": [sg_name]},
            {"Name": "vpc-id", "Values": [vpc_id]},
        ]
    )
    if sgs["SecurityGroups"]:
        sg_id = sgs["SecurityGroups"][0]["GroupId"]
        print(f"  Security group exists: {sg_id}")
        return sg_id

    # Create it
    sg = ec2.create_security_group(
        GroupName=sg_name,
        Description="Allow PostgreSQL access for MYBank Aurora",
        VpcId=vpc_id,
    )
    sg_id = sg["GroupId"]

    # Allow PostgreSQL from anywhere (dev only — restrict in production)
    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 5432,
                "ToPort": 5432,
                "IpRanges": [
                    {"CidrIp": "0.0.0.0/0", "Description": "PostgreSQL dev access"}
                ],
            }
        ],
    )
    print(f"  Created security group: {sg_id}")
    return sg_id


def main():
    print("=" * 60)
    print("Provisioning Aurora PostgreSQL Serverless v2")
    print(f"Region: {REGION}")
    print("=" * 60)

    rds = boto3.client("rds", region_name=REGION)
    ec2 = boto3.client("ec2", region_name=REGION)

    # Check if cluster already exists
    try:
        existing = rds.describe_db_clusters(DBClusterIdentifier=CLUSTER_ID)
        endpoint = existing["DBClusters"][0]["Endpoint"]
        print(f"\nCluster already exists!")
        print(f"  Endpoint: {endpoint}")
        print(f"\nAdd to .env:")
        print(f"  AURORA_HOST={endpoint}")
        print(f"  AURORA_USER={DB_USER}")
        print(f"  AURORA_PASSWORD=<your-password>")
        return
    except rds.exceptions.DBClusterNotFoundFault:
        pass

    password = generate_password()
    print(f"\n[1/5] Generated credentials")
    print(f"  User: {DB_USER}")
    print(f"  Password: {password}")

    # Get VPC and subnets
    print("\n[2/5] Getting VPC configuration...")
    vpc_id, subnet_ids = get_default_vpc_subnets(ec2)
    sg_id = get_or_create_security_group(ec2, vpc_id)

    # Create subnet group
    print("\n[3/5] Creating DB subnet group...")
    try:
        rds.create_db_subnet_group(
            DBSubnetGroupName=SUBNET_GROUP,
            DBSubnetGroupDescription="Subnet group for MYBank Aurora",
            SubnetIds=subnet_ids,
        )
        print(f"  Created subnet group: {SUBNET_GROUP}")
    except rds.exceptions.DBSubnetGroupAlreadyExistsFault:
        print(f"  Subnet group already exists: {SUBNET_GROUP}")

    # Create Aurora Serverless v2 cluster
    print("\n[4/5] Creating Aurora Serverless v2 cluster...")
    rds.create_db_cluster(
        DBClusterIdentifier=CLUSTER_ID,
        Engine=ENGINE,
        EngineVersion=ENGINE_VERSION,
        MasterUsername=DB_USER,
        MasterUserPassword=password,
        DatabaseName=DB_NAME,
        DBSubnetGroupName=SUBNET_GROUP,
        VpcSecurityGroupIds=[sg_id],
        ServerlessV2ScalingConfiguration={
            "MinCapacity": MIN_ACU,
            "MaxCapacity": MAX_ACU,
        },
        StorageEncrypted=True,
        EnableHttpEndpoint=True,
    )
    print(f"  Cluster {CLUSTER_ID} creation initiated")

    # Create instance
    print("\n[5/5] Creating Serverless v2 instance...")
    rds.create_db_instance(
        DBInstanceIdentifier=INSTANCE_ID,
        DBClusterIdentifier=CLUSTER_ID,
        DBInstanceClass="db.serverless",
        Engine=ENGINE,
        PubliclyAccessible=True,
    )
    print(f"  Instance {INSTANCE_ID} creation initiated")

    # Wait for cluster
    print("\nWaiting for cluster to become available (this takes 5-10 minutes)...")
    waiter = rds.get_waiter("db_cluster_available")
    waiter.wait(
        DBClusterIdentifier=CLUSTER_ID,
        WaiterConfig={"Delay": 30, "MaxAttempts": 30},
    )

    # Get endpoint
    cluster = rds.describe_db_clusters(DBClusterIdentifier=CLUSTER_ID)
    endpoint = cluster["DBClusters"][0]["Endpoint"]

    print("\n" + "=" * 60)
    print("Aurora PostgreSQL Serverless v2 is ready!")
    print("=" * 60)
    print(f"\nEndpoint: {endpoint}")
    print(f"Database: {DB_NAME}")
    print(f"User: {DB_USER}")
    print(f"Password: {password}")
    print(f"\nAdd to .env:")
    print(f"  AURORA_HOST={endpoint}")
    print(f"  AURORA_PORT=5432")
    print(f"  AURORA_DATABASE={DB_NAME}")
    print(f"  AURORA_USER={DB_USER}")
    print(f"  AURORA_PASSWORD={password}")


if __name__ == "__main__":
    main()
