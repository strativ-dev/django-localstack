import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import DocumentForm
from .models import Document
from .utils import get_s3_client

logger = logging.getLogger(__name__)


def upload_file(request):
    """Handle file upload, save to S3 with correct Content-Type, and log the operation."""
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            try:
                # Upload file to S3 with Content-Type
                s3 = get_s3_client()

                # Set the correct Content-Type based on the file
                content_type = file.content_type

                s3.put_object(
                    Bucket="mybucket",
                    Key=file.name,
                    Body=file,
                    ContentType=content_type,  # Ensure correct Content-Type
                    ACL="public-read",  # Ensure the file is publicly accessible
                )

                # Save metadata in the database (not the file itself)
                document = Document.objects.create(file=file.name)

                logger.info(f"File uploaded to S3: {document.file.name}")

                return redirect("upload_success")
            except Exception as e:
                logger.error(f"Error uploading file to S3: {e}")
                return HttpResponse(f"File upload failed: {e}", status=500)
        else:
            logger.error("Form is invalid.")
            return HttpResponse("Form is invalid.", status=400)

    # If not POST, render the empty form
    form = DocumentForm()
    return render(request, "fileupload.html", {"form": form})


def upload_success(request):
    return render(request, "fileupload_success.html")


def list_files(request):
    documents = Document.objects.all()
    return render(request, "list_files.html", {"documents": documents})
