from django.contrib import admin
from django.urls import path

from newspaper.views import index, RedactorListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
]

app_name = "newspaper"
