from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Redactor, Topic, Newspaper


def index(request: HttpRequest) -> HttpResponse:
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()
    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
    }
    return render(request, "newspaper/index.html", context)
