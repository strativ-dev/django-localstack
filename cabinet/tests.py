import pytest
from moto import mock_aws
from cabinet.models import Photo
from django.conf import settings

@pytest.mark.django_db
class TestCabinet:
    @mock_aws
    def test_cabinet_photo(self):
        Photo.objects.create(
            image="images/test.jpg",
            title="Test",
        )
        assert Photo.objects.count() == 1
        assert Photo.objects.first().image.url.startswith(f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/images/")
