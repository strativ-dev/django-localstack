from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Document(models.Model):
    document = models.FileField(upload_to="documents/")
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Video(models.Model):
    video = models.URLField()
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
