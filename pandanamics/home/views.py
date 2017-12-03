from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic
from django.apps import apps

Post = apps.get_model('blog', 'Post')

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    context = {
        'topics': Topic.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', context) # location of html template

def contact(request):
    return render(request, 'home/basic.html',
                  {'content':['If you would like to contact me, please email me',
                              'emailplaceholder@gmail.com']})
def allTopics(request):
    context = {
        'topics': Topic.objects.all()
    }
    return render(request, 'home/all_topics.html',context)

def topic(request, title):
    topic = Topic.objects.get(title=title)
    context = {
        'topic': topic
    }
    return render(request, 'home/topic.html', context)