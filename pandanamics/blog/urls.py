from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Post # Our class

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                            template_name="blog/blog.html")), # Sort by descending date
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                                         template_name = 'blog/post.html'))] # ?P means named groups. <pk> is primary key. First column of table