import pytest
from moto import mock_aws
from cabinet.models import Photo, Document, Video
from django.core.files.uploadedfile import InMemoryUploadedFile

@pytest.mark.django_db
class TestCabinet:
    def test_cabinet(self):
        assert True

    @mock_aws
    def test_cabinet_photo(self):
        Photo.objects.create(
            image="images/test.jpg",
            title="Test",
        )
        assert Photo.objects.count() == 1
        assert Photo.objects.first().image.url == "images/test.jpg"
