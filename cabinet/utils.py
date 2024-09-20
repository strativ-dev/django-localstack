import boto3


def get_s3_client():
    """Return a boto3 S3 client configured for LocalStack."""
    return boto3.client("s3", endpoint_url="http://localhost:4566/")
