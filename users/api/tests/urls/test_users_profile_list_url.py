from django.test import TestCase
from django.urls import reverse, resolve
from users.api.views import UsersProfileListAPIView


class TestUserProfileListUrl(TestCase):

    def setUp(self):
        self.url = '/users/api/'

    def test_reverse_user_profile_api_url(self):
        user_profile_api_url = reverse(
            'users:api:list'
        )

        self.assertEqual(
            user_profile_api_url,
            self.url
        )

    def test_resolve_user_profile_api_url(self):
        found = resolve(self.url)

        self.assertEqual(
            found.func.__name__,
            UsersProfileListAPIView.as_view().__name__
        )
