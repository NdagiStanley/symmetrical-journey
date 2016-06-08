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

    def authenticate_api_call(self, view, url):
        request = factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        force_authenticate(response, user=self.user)
        self.assertEqual(response.status_code, 200)

    def test_view_category(self):
        """
        Ensure we can get to category endpoint.
        """
        url = reverse('category')
        response = self.client.get(url)
        view = CategoryListAPIView.as_view()
        self.assertEqual(response.status_code, 403)
        self.authenticate_api_call(view, url)

    def test_view_picture(self):
        """
        Ensure we can get to picture endpoint.
        """
        url = reverse('category')
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        client.force_authenticate(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

