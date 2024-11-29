import os
from django.db import models
from django.utils.html import strip_tags
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field


def thumbnail_upload_to(instance, filename):
    # Her blog için ayrı bir klasör oluşturabilir
    return f"thumbnails/{instance.title}/{filename}"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field(
        'Content',
        config_name='default',  # CKEditor konfigürasyonu
        blank=True,
    )
    date_published = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_to, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    @property
    def description(self):
        plain_text = strip_tags(self.content)  # HTML etiketlerini kaldıran bir şey o yüzden eklendi.
        return f"{plain_text[:300]}..." if len(plain_text) > 300 else plain_text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.thumbnail and os.path.exists(self.thumbnail.path):
            img = Image.open(self.thumbnail.path)
            if img.height > 480 or img.width > 640:
                output_size = (640, 480)
                img.thumbnail(output_size)
                img.save(self.thumbnail.path, quality=90)
