from __future__ import unicode_literals

from django.db import models
from sjourney import settings

from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '<Category {}>'.format(self.name)

    @property
    def images(self):
        images = []
        for picture in self.pictures.all():
            images.append(
                {'id': picture.id,
                 'name': picture.title,
                 'date_created': picture.date_created,
                 'date_modified': picture.date_modified,
                 'editted': picture.editted})
        return images


class Picture(models.Model):
    """docstring for Picture model"""

    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, related_name="pictures", default=1)
    uploaded_image = models.ImageField(upload_to='pics/', blank=False)
    editted_image = models.ImageField(upload_to='editted/', blank=True)
    editted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Delete photos when uploader is deleted
    uploader = models.ForeignKey(
        User,
        related_name="photos",
        on_delete=models.CASCADE)


class SocialAuthUser(models.Model):
    """
    Read-only ORM to query information that is populated by python-social-auth
    in the 'social_auth_usersocialauth' table.
    """
    id = models.IntegerField(primary_key=True)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(User, models.DO_NOTHING)

    def __str__(self):
        return '<User #{0} - Social Auth Provider {1}>'.format(
            self.uid, self.provider)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
