from django.contrib import admin
from django.urls import path

from newspaper.views import (
    index,
    RedactorListView,
    TopicListView,
    NewspaperListView,
    RedactorDetailView,
    NewspaperDetailView,
    NewspaperCreateView,
    RedactorCreateView,
    TopicCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path(
        "redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create" ),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("newspapers", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),


]

app_name = "newspaper"
