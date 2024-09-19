# upload/views.py

from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


import logging

logger = logging.getLogger(__name__)


def upload_file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            logger.info(f"File uploaded: {document.file.name}")
            print(f"File uploaded: {document.file.name}")
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
