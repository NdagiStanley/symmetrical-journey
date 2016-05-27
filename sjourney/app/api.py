from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from serializers import UserSerializer, SocialAuthUserSerializer
from serializers import PictureSerializer, CategorySerializer
from models import Picture, SocialAuthUser, Category


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class SocialAuthUserListAPIView(generics.ListAPIView):
    queryset = SocialAuthUser.objects.all()
    serializer_class = SocialAuthUserSerializer


class SocialAuthUserDetailAPIView(generics.RetrieveAPIView):
    queryset = SocialAuthUser.objects.all()
    serializer_class = SocialAuthUserSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PictureListAPIView(generics.ListCreateAPIView):
    """
    docstring for PictureListAPIView
    endpoint = '/api/v1/pics/' path
    """

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        """The user will be associated with the photo as the uploader"""
        serializer.save(uploader=self.request.user)


class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    docstring for PictureDetailAPIView
    endpoint = '/api/v1/pics/<id>' path
    """

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
