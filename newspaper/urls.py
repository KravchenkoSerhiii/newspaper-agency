from django.contrib import admin
from django.urls import path

from newspaper.views import index, RedactorListView, TopicListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path("topics/", TopicListView.as_view(), name="topic-list")
]

app_name = "newspaper"
