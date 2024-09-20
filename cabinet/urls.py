from django.urls import path

from cabinet.views import DocumentListView, FileUploadView, UploadSuccessView
from cabinet.api_views import DocumentModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"documents", DocumentModelViewSet, basename="document")


urlpatterns = [
    path("", FileUploadView.as_view(), name="file_upload"),  # Upload view
    path("upload-success/", UploadSuccessView.as_view(), name="upload_success"),
    path("list-files/", DocumentListView.as_view(), name="list_files"),
] + router.urls
