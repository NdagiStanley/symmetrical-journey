from __future__ import unicode_literals

from django.db import models
from sjourney import settings

# fb_user = settings.AUTH_USER_MODEL
from django_facebook.models import FacebookModel

# Create your models here.
class Picture(models.Model):
    """docstring for Picture model"""

    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255, blank=True)
    uploaded_image = models.ImageField(upload_to='pics/', blank=False)
    editted_image = models.ImageField(upload_to='ediited/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Delete photos when uploader is deleted
    uploader = models.ForeignKey(
        FacebookModel,
        related_name="photos",
        on_delete=models.CASCADE)
