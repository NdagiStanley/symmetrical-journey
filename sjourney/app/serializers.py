from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Picture, SocialAuthUser, Category


class CategorySerializer(serializers.ModelSerializer):
    """docstring for CategorySerializer"""

    class Meta:
        model = Category
        fields = ('id', 'name', 'images')


class PictureSerializer(serializers.ModelSerializer):
    """docstring for PictureSerializer"""

    class Meta:
        model = Picture
        fields = ('id', 'uploader', 'uploaded_image', 'editted_image',
                  'date_created', 'date_modified', 'size', 'category')

        read_only_fields = ('id', 'date_created')

    def create(self, validated_data):
        picture = Picture(
            uploaded_image=validated_data['uploaded_image'],
            uploader=self.context.get('request').user,
            )
        picture.save()
        return picture


class UserSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

        write_only_fields = ('password')

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(
                email=validated_data['email'],
                username=validated_data['username'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user


class SocialAuthUserSerializer(serializers.ModelSerializer):
    """docstring for SocialAuthUserSerializer"""

    class Meta:
        model = SocialAuthUser
        fields = ('id', 'uid', 'provider', 'user')
