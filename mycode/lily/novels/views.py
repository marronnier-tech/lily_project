from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views import View

from .models import Story


def index(request):
    latest_story_list = Story.objects.order_by("-favorite")
    output = ', '.join([l.title for l in latest_story_list])
    template = loader.get_template('novels/index.html')
    context = {
        'latest_story_list': latest_story_list,
    }
    return HttpResponse(template.render(context, request))


"""
def story_map(request, story_id):
    return HttpResponse("You're looking at the story %s." % title)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""
