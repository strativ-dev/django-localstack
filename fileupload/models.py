from django.db import models
from django.core.files.storage import FileSystemStorage


class Document(models.Model):
    file = models.FileField(storage=FileSystemStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
