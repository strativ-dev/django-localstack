from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_file, name="upload_file"),
    path("upload/success/", views.upload_success, name="upload_success"),
    path("files/", views.list_files, name="list_files"),  # New URL for listing files
]
