from django.urls import path
from .views import FileUploadView, upload_success, list_files

urlpatterns = [
    path("", FileUploadView.as_view(), name="file_upload"),  # Upload view
    path("upload/success/", upload_success, name="upload_success"),
    path("files/", list_files, name="list_files"),  # New URL for listing files
]
