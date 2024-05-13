from django.contrib.admin import site
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from newspaper.models import Newspaper


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="test_admin",
            password="testpassword"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="test_redactor",
            password="password1234",
            years_of_experience="8",
            first_name="Test",
            last_name="Redactor",
        )

    def test_years_of_experience_listed(self):
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)


class NewspaperAdminSiteTests(TestCase):
    def test_search_fields(self):
        self.assertIn("title", site._registry[Newspaper].search_fields)
