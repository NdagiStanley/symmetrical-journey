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
        SocialAuthUser.objects.all().delete()
        Category.objects.all().delete()
        Picture.objects.all().delete()

    def test_user_string_representation(self):
        """Test the representation of user instance"""
        self.assertEqual(str(self.user), self.user.username)

    def test_user_fields(self):
        """Test the fields of user model"""
        self.assertEqual(self.user.username, 'md')

    def social_auth_user_string_representation(self):
        """Test the representation of social_auth_user instance"""
        self.assertEqual(str(self.suser),
            '<User #{} - Social Auth Provider {}>'.format(
                self.suser.uid, self.suser.provider))

    def social_auth_user_fields(self):
        """Test the fields of social_auth_user model"""
        self.assertEqual(self.suser.id, 1)
        self.assertEqual(self.suser.user, 1)
        self.assertEqual(self.suser.provider, "facebook")

    def test_picture_fields(self):
        """Test the fields of picture model"""
        self.assertEqual(self.picture.editted, False)
        self.assertEqual(self.picture.uploader, self.user)

    def test_category_string_representation(self):
        """Test the representation of Category instance"""
        self.assertEqual(str(self.category),
                         '<Category {}>'.format(self.category.name))

    def test_category_fields(self):
        """Test the fields of category model"""
        self.assertEqual(self.picture.editted, False)
        self.assertEqual(self.picture.uploader, self.user)
