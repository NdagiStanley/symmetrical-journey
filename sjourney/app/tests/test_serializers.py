import os
from PIL import Image
from django.core.files import File
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from sjourney.app.models import Picture, SocialAuthUser, Category
from sjourney.app.serializers import PictureSerializer, CategorySerializer
from sjourney.app.serializers import UserSerializer, SocialAuthUserSerializer


class SerializerTests(APITestCase):
    invalid_data = {'test_foo': 'bar'}

    def setUp(self):
        self.user = User.objects.create(username="md", password="md")
        self.category = Category.objects.create(name="Mine", owner=self.user)
        size = (200, 200)
        img = Image.new("RGBA", size)
        img.save('media/test.jpg')

    def tearDown(self):
        """Clean the test db"""
        User.objects.all().delete()
        Category.objects.all().delete()
        Picture.objects.all().delete()
        os.system("rm media/test.jpg")


    def test_picture_serializers(self):
        data = {"uploader": self.user, "name": 'Pic1',
        "uploaded_image": File(open('media/test.jpg')),
        "edited_image": None, "date_created": "2016-06-09T15:53:23.006896Z",
        "date_modified": "2016-06-09T15:53:56.895683Z",
        "category": 1}
        serializer = PictureSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        serializer = PictureSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_category_serializers(self):
        data = {"name": "New", "owner": self.user}
        serializer = CategorySerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_user_serializers(self):
        data = {"username": "stanmd", "password": "md"}
        serializer = UserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_suser_serializers(self):
        data = {"id": 2, "uid": 2, "provider": "facebook", "user": 1}
        serializer = SocialAuthUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        serializer = SocialAuthUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
