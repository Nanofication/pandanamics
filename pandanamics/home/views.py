from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic, Post
from django.apps import apps

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
    posts = Post.objects.filter(topic__title=topic.title)
    context = {
        'topic': topic,
        'posts': posts
    }
    return render(request, 'home/topic.html', context)

def post(request, post_title):
    post = Post.objects.get(title=post_title)
    context = {
        'post': post
    }
    return render(request, 'home/post.html', context)