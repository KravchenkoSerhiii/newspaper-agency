from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"Username: {self.username}: {self.first_name} {self.last_name}."


class Topic(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Topic: {self.name}."


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="publishers")

    def __str__(self):
        return f"Title: {self.title}, {self.topic}, {self.published_date}"
