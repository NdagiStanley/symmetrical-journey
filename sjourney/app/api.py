from rest_framework import generics

from .serializers import PictureSerializer
from .models import Picture


class PictureListAPIView(generics.ListCreateAPIView):
    """
    docstring for PictureListAPIView
    endpoint = '/api/v1/pics/' path
    """

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        """The user will be associated with the photo as the uploader"""
        serializer.save(uploader= self.request.user)


class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    docstring for PictureDetailAPIView
    endpoint = '/api/v1/pics/<id>' path
    """

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
