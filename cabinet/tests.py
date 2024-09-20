import boto3
import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from moto import mock_aws

from cabinet.models import Document


# Mock S3 setup as a pytest fixture
@pytest.fixture
def mock_s3_bucket():
    with mock_aws():
        s3 = boto3.client("s3", region_name="us-east-1")
        # Create the mock bucket
        s3.create_bucket(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        yield s3


# Test using pytest
def test_document_upload(mock_s3_bucket, db):
    # Create a mock file
    mock_file = SimpleUploadedFile("testfile.txt", b"File content for testing")

    # Create and save the document instance
    document = Document.objects.create(title="Test Document", document=mock_file)
    document.save()

    # Check if the file was "uploaded" to the mock S3
    files_in_s3 = [
        obj["Key"]
        for obj in mock_s3_bucket.list_objects_v2(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME
        ).get("Contents", [])
    ]
    assert f"documents/{mock_file.name}" in files_in_s3

    # Check that the file content is correct (retrieving from S3)
    s3_object = mock_s3_bucket.get_object(
        Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=f"documents/{mock_file.name}"
    )
    file_content = s3_object["Body"].read().decode("utf-8")
    assert file_content == "File content for testing"
