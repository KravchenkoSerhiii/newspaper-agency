from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.forms import RedactorSearchForm

REDACTOR_URL = reverse("newspaper:redactor-list")


class PublicRedactorTest(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertEqual(res.status_code, 302)


class PrivateRedactorTest(TestCase):
    def setUp(self):
        self.redactor = get_user_model().objects.create_user(
            username="test_user",
            password="password12",
        )
        self.client.force_login(self.redactor)
        self.response = self.client.get(REDACTOR_URL)

    def test_redactor_authenticated_user_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_redactor_context_data(self):
        form = self.response.context["search_form"]
        self.assertIsInstance(form, RedactorSearchForm)
        self.assertEqual(form.initial["username"], "")
