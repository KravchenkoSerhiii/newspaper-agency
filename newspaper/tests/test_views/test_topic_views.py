from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from newspaper.forms import TopicSearchForm
from newspaper.models import Topic
from newspaper.views import TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView

TOPIC_URL = reverse("newspaper:topic-list")


class PublicTopicTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="password123",
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(
            name="Test-topic",
        )
        self.response = self.client.get(TOPIC_URL)

    def test_topic_template_used(self):
        self.assertTemplateUsed(self.response, "newspaper/topic_list.html")

    def test_topic_authenticated_user_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_topic_context(self):
        topics = Topic.objects.all()
        self.assertEqual(
            list(self.response.context["topic_list"]),
            list(topics)
        )

    def test_topic_paginate(self):
        self.assertEqual(TopicListView.paginate_by, 5)

    def test_topic_context_data(self):
        form = self.response.context["search_form"]
        self.assertIsInstance(form, TopicSearchForm)
        self.assertEqual(form.initial["name"], "")

    def test_topic_create_success_url(self):
        view = TopicCreateView()
        view.object = self.topic
        self.assertEqual(view.get_success_url(), TOPIC_URL)

    def test_topic_update_success_url(self):
        view = TopicUpdateView()
        view.object = self.topic
        self.assertEqual(view.get_success_url(), TOPIC_URL)

    def test_topic_delete_success_url(self):
        view = TopicDeleteView()
        view.object = self.topic
        self.assertEqual(view.get_success_url(), TOPIC_URL)
