from django.conf.urls import url, include
from . import views # Returning views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
