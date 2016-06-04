import datetime
import tempfile

from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Category, Picture, User, SocialAuthUser


class ModelTest(TestCase):
    """Test Models"""

    def setUp(self):
        """Create instances of the models"""
        self.user = User.objects.create(username="md", password="md")
        self.category = Category.objects.create(name="Personal")
        self.picture = Picture.objects.create(
            uploaded_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            uploader=self.user, category=self.category)

    def tearDown(self):
        """Clean the test db"""
        User.objects.all().delete()
        Category.objects.all().delete()
        Picture.objects.all().delete()

    def test_user_string_representation(self):
        """Test the representation of user instance"""
        self.assertEqual(str(self.user), self.user.username)

    def test_user_fields(self):
        """Test the fields of user model"""
        self.assertEqual(self.user.username, 'md')

    def test_picture_string_representation(self):
        """Test the representation of picture instance"""
        self.assertEqual(str(self.picture),
                         '<Picture {}>'.format(self.picture.name))

    def test_picture_fields(self):
        """Test the fields of picture model"""
        self.assertEqual(self.picture.edited, False)
        self.assertIsNot(self.picture.uploaded_image, None)
        self.assertEqual(self.picture.uploader.id, 1)
        self.assertEqual(self.picture.category.id, 1)

    def test_category_string_representation(self):
        """Test the representation of Category instance"""
        self.assertEqual(str(self.category),
                         '<Category {}>'.format(self.category.name))

    def test_category_fields(self):
        """Test the fields of category model"""
        self.assertEqual(self.category.name, 'Personal')
        self.assertEqual(len(self.category.images), 1)
