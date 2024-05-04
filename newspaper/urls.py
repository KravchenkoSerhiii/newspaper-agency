from django.contrib import admin
from django.urls import path

from newspaper.views import index

urlpatterns = [
    path("", index),
]