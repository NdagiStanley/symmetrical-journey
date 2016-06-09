from __future__ import unicode_literals

from django.db import models
from sjourney import settings

from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    """docstring for Category model"""
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, related_name="categories")

    def __str__(self):
        return '<Category {}>'.format(self.name)

    @property
    def images(self):
        images = []
        for picture in self.pictures.all():
            images.append(
                {'id': picture.id,
                 'name': picture.name,
                 'date_created': picture.date_created,
                 'date_modified': picture.date_modified,
                 'picture': picture.uploaded_image})
        return images


class Picture(models.Model):
    """docstring for Picture model"""

    size = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, related_name="pictures")
    uploaded_image = models.ImageField(upload_to='pics/', blank=False)
    edited_image = models.ImageField(upload_to='edited/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Delete photos when uploader is deleted
    uploader = models.ForeignKey(User, related_name="photos")

    def __str__(self):
        return '<Picture {}>'.format(self.name)


class SocialAuthUser(models.Model):
    """
    ORM to query information that is populated by python-social-auth
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
