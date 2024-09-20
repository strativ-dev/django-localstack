import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import DocumentForm
from .models import Document
from .services import FileUploadService

logger = logging.getLogger(__name__)


class FileUploadView(View):
    """Handle file upload using a class-based view."""

    def get(self, request):
        form = DocumentForm()
        return render(request, "cabinet/fileupload.html", {"form": form})

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get("document")

            if not file:
                logger.error("No file uploaded.")
                return HttpResponse("No file uploaded.", status=400)

            try:
                # Move the file handling logic to a service
                FileUploadService.upload_to_s3(file)
                return redirect("upload_success")
            except Exception as e:
                logger.error(f"Error uploading file: {e}")
                return HttpResponse(f"File upload failed: {e}", status=500)
        else:
            logger.error("Form is invalid.")
            return HttpResponse("Form is invalid.", status=400)


def upload_success(request):
    return render(request, "cabinet/fileupload_success.html")


def list_files(request):
    documents = Document.objects.all()
    return render(request, "cabinet/list_files.html", {"documents": documents})


# Create your views here.
