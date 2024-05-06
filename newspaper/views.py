from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic

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


class RedactorListView(generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"


class RedactorDetailView(generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"


class NewspaperListView(generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_list.html"
