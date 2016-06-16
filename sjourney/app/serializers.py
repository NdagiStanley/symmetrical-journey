import os
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Picture, SocialAuthUser, Category


class PictureSerializer(serializers.ModelSerializer):
    """docstring for PictureSerializer"""

    class Meta:
        model = Picture
        fields = ('id', 'uploader', 'name', 'uploaded_image', 'edited_image',
                  'date_created', 'date_modified', 'category')

        read_only_fields = ('id', 'edited_image',
            'date_created', 'name', 'uploader', 'size')

    def create(self, validated_data):
        picture = Picture(
            uploaded_image=validated_data['uploaded_image'],
            uploader=self.context.get('request').user,
            name=os.path.basename(validated_data['uploaded_image'].name),
            # size=os.path.basename(validated_data['uploaded_image'].size),
            # category=validated_data['category']
        )
        picture.save()
        return picture

    def update(serializer, *args, **kwargs):
        user_id = serializer.request.user.id
        picture_id = kwargs['id']
        picture = Picture.objects.filter(
            uploader=user_id, id=picture_id)
        if picture:
            picture.uploaded_image = serializer.request.data.get(
                'uploaded_image', picture.uploaded_image)
            picture.save()
            return Response(
                {"message": "Picture '{}' updated successfully".format(picture.id)},
                    status = status.HTTP_200_OK)
        return Response({"error": "You cannot update this picture"},
            status = status.HTTP_404_NOT_FOUND)


class CategorySerializer(serializers.ModelSerializer):
    """docstring for CategorySerializer"""

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner')

        read_only_fields = ('id', 'owner')

    def create(self, validated_data):
        category = Category(
            name=validated_data['name'],
            owner=self.context.get('request').user)
        category.save()
        return category


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
