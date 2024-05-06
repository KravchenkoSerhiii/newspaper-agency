from django.contrib import admin
from django.urls import path

from newspaper.views import index, RedactorListView, TopicListView, NewspaperListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("newspapers", NewspaperListView.as_view(), name="newspaper-list"),
]

app_name = "newspaper"
