from django.urls import path
from .views import FileUploadView, UploadSuccessView, DocumentListView

urlpatterns = [
    path("", FileUploadView.as_view(), name="file_upload"),  # Upload view
    path("upload-success/", UploadSuccessView.as_view(), name="upload_success"),
    path("list-files/", DocumentListView.as_view(), name="list_files"),
]
