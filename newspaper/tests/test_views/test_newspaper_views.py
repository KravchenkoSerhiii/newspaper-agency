from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.forms import NewspaperSearchForm
from newspaper.models import Newspaper, Topic, Redactor
from newspaper.views import NewspaperListView, NewspaperDeleteView, NewspaperUpdateView, NewspaperCreateView

NEWSPAPER_URL = reverse("newspaper:newspaper-list")


class PublicNewspaperTest(TestCase):
    def test_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateNewspaperTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="password123",
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(
            name="test_topic",
        )
        self.newspaper = Newspaper.objects.create(
            title="test_title",
            topic=self.topic,
        )
        self.response = self.client.get(NEWSPAPER_URL)

    def test_newspaper_authenticated_user_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_newspaper_paginate(self):
        self.assertEqual(NewspaperListView.paginate_by, 5)

    def test_newspaper_context_data(self):
        form = self.response.context["search_form"]
        self.assertIsInstance(form, NewspaperSearchForm)
        self.assertEqual(form.initial["title"], "")

    def test_newspaper_create_success_url(self):
        view = NewspaperCreateView()
        view.object = self.newspaper
        self.assertEqual(view.get_success_url(), NEWSPAPER_URL)

    def test_newspaper_update_success_url(self):
        view = NewspaperUpdateView()
        view.object = self.newspaper
        self.assertEqual(view.get_success_url(), NEWSPAPER_URL)

    def test_newspaper_delete_success_url(self):
        view = NewspaperDeleteView()
        view.object = self.newspaper
        self.assertEqual(view.get_success_url(), NEWSPAPER_URL)
