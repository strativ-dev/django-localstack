# upload/views.py
import boto3
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


import logging

logger = logging.getLogger(__name__)


import logging
from django.http import HttpResponse
from .forms import DocumentForm

logger = logging.getLogger(__name__)

from django.core.files.storage import default_storage


def upload_file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            s3 = boto3.client("s3", endpoint_url="http://localhost:4566/")
            s3.put_object(Bucket="mybucket", Key=file.name, Body=file)
            document = form.save()
            print(default_storage.__class__)
            logger.info(f"File uploaded: {document.file.name}")
            print(f"File uploaded: {document.file.name}")
            logger.info(f"File path: {document.file.path}")
            logger.info(f"File URL: {document.file.url}")
            return redirect("upload_success")
        else:
            logger.error("Form is invalid.")
            print("Form is invalid.")
    else:
        form = DocumentForm()
    return render(request, "fileupload.html", {"form": form})


def upload_success(request):
    return render(request, "fileupload_success.html")


def list_files(request):
    documents = Document.objects.all()
    return render(request, "list_files.html", {"documents": documents})
