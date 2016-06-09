import tempfile
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.test import force_authenticate, APIClient
from sjourney.app.models import Category, Picture, User
from sjourney.app.api import CategoryListAPIView


factory = APIRequestFactory()
client = APIClient()


class APICallTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="md", password="md")
        self.category = Category.objects.create(name="Personal", owner=self.user)
        self.picture = Picture.objects.create(
            uploaded_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            uploader=self.user, category=self.category)

    def tearDown(self):
        client.logout()

    def authenticate_api_call(self, view, url):
        request = factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        force_authenticate(response, user=self.user)
        self.assertEqual(response.status_code, 200)

    def test_view_category(self):
        """
        Ensure we can get to categories endpoint
        """
        url = reverse('category')
        response = self.client.get(url)
        view = CategoryListAPIView.as_view()
        self.assertEqual(response.status_code, 403)
        self.authenticate_api_call(view, url)

    def test_single_category(self):
        """
        Ensure we can get to single category endpoint
        """
        url = '/api/v1/categories/1'
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_picture(self):
        """
        Ensure we can get to pictures endpoint
        """
        url = reverse('picture')
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_single_picture(self):
        """
        Ensure we can get to single picture endpoint
        """
        url = '/api/v1/pics/1'
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_users(self):
        """
        Ensure we can get to users endpoint
        """
        url = reverse('user')
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_view_users_from_social_accounts(self):
        """
        Ensure we can get to susers endpoint
        """
        url = reverse('suser')
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_single_suser(self):
        """
        Ensure we can get to single susert endpoint
        """
        url = '/api/v1/susers/1'
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
