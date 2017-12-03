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
def topic(request, title):
    topic = Topic.objects.get(title=title)
    return render(request, 'blog/topic.html',{'title': topic})