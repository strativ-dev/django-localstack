from django.contrib import admin

from cabinet.models import Document, Photo, Video

admin.site.register(Photo)
admin.site.register(Document)
admin.site.register(Video)
