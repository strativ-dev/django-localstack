import boto3
from .models import Document
import logging

logger = logging.getLogger(__name__)


class FileUploadService:
    @staticmethod
    def get_s3_client():
        # Assuming you have AWS credentials configured for boto3
        return boto3.client("s3", endpoint_url="http://localhost:4566/")

    @staticmethod
    def upload_to_s3(file):
        """Uploads the file to S3 and saves metadata to the database."""
        s3 = FileUploadService.get_s3_client()
        content_type = file.content_type
        directory_path = "documents/"

        # Upload file to S3
        s3.put_object(
            Bucket="django-localstack",
            Key=f"{directory_path}{file.name}",
            Body=file,
            ContentType=content_type,
            ACL="public-read",
        )

        # Save file metadata in the database
        document = Document.objects.create(document=f"{directory_path}{file.name}")
        logger.info(f"File uploaded to S3: {document.document}")
