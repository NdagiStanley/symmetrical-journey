from rest_framework import serializers

from .models import Picture

class PictureSerializer(serializers.ModelSerilizer):
    """docstring for PictureSerializer"""

    class Meta:
        model = Picture
        fields =('id', 'uploader', 'uploaded_image', 'editted_image', 'date_created', 'date_modified', 'size')

        read_only_fields = ('id', 'date_created')
