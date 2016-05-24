from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    """docstring for PictureSerializer"""

    class Meta:
        model = Picture
        fields = ('id', 'uploader', 'uploaded_image', 'editted_image',
                  'date_created', 'date_modified', 'size')

        read_only_fields = ('id', 'date_created')


class UserSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
