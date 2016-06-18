from django.test import TestCase
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from sjourney.app.models import User


class LoginTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_facebook_login(self):
        """
        Test that the user can login via facebook
        """
        response = self.client.get('/login/facebook/')
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        """
        Test that the user can logout via route
        """
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_app_access(self):
        """
        Test that '/app/' can only be accessed by an authenticated user
        """
        self.assertEqual(len(User.objects.all()), 1)
        response = self.client.get(reverse('app'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/?next=/app/')

        self.client.login(username='md', password='me')
        auth_response = self.client.get(reverse('app'))
        self.assertEqual(auth_response.status_code, 200)
