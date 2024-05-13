from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Redactor, Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test topic")
        self.assertEqual(str(topic), topic.name)


class RedactorTests(TestCase):
    EMAIL = "test@mail.com"

    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="test_user",
            password="testpass123",

        )

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor),
                         f"{self.redactor.username} "
                         f"({self.redactor.first_name} {self.redactor.last_name})"
                         )

    def test_get_absolute_url(self):
        expected_url = reverse(
            "newspaper:redactor-detail",
            kwargs={"pk": self.redactor.pk}
        )
        self.assertEqual(self.redactor.get_absolute_url(), expected_url)

    def test_verbose_name(self):
        self.assertEqual(Redactor._meta.verbose_name, "redactor")

    def test_verbose_name_plural(self):
        self.assertEqual(Redactor._meta.verbose_name_plural, "redactors")


class NewspaperTests(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="test_redactor",
            password="testpas789",
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="TestTopic")
        newspaper = Newspaper.objects.create(title="TestTitle", topic=topic)
        self.assertEqual(str(newspaper), newspaper.title)
