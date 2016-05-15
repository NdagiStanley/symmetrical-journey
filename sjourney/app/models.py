from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):
    """docstring for Picture model"""

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    uploaded_image = models.ImageField()
    editted_image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # Delete photos when uploader is deleted
    uploader = models.ForeignKey(User, related_name="photos", on_delete=models.CASCADE)
