import os
import effects
from sjourney.settings import MEDIA_URL
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from serializers import UserSerializer, SocialAuthUserSerializer
from serializers import PictureSerializer, CategorySerializer
from models import Picture, SocialAuthUser, Category
from authentication import CsrfExemptSessionAuthentication

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
    # authentication_classes = (CsrfExemptSessionAuthentication,)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes = (CsrfExemptSessionAuthentication,)


class PictureListAPIView(generics.ListCreateAPIView):
    """
    docstring for PictureListAPIView
    endpoint = '/api/v1/pics/' path
    """

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)


class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    docstring for PictureDetailAPIView
    endpoint = '/api/v1/pics/<id>' path or
    endpoint = '/api/v1/pics/<id>?filter="filter_id"' path
    """

    serializer_class = PictureSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get_queryset(self):
        """
        This view should return one or a list of all the filters for
        the image as determined by the filter portion of the URL.
        """
        all_pictures = Picture.objects.all()
        filter = self.request.query_params.get('filter', None)
        if not filter:
            return all_pictures
        elif int(filter) > 10 or int(filter) <= 0:
            return all_pictures
        picture = Picture.objects.filter(id=self.kwargs['pk']).first()
        name = os.path.splitext(str(picture.uploaded_image))
        name = '-edited'.join(list(name))
        effects.Effect(int(filter), picture.uploaded_image).save(
            os.path.join(MEDIA_URL, name).lstrip('/'))
        picture.edited_image = os.path.join(MEDIA_URL, name)
        picture.save()
        return all_pictures
