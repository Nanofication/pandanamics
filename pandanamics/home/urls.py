from django.conf.urls import url, include
from . import views # Returning views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^topics/', views.allTopics, name='allTopics'),
    url(r'^(?P<title>[-\w]+)/$', views.topic, name='topic'),
    url(r'^([-\w]+)/(?P<post_title>[-\w]+)/$', views.post, name='post')
]
