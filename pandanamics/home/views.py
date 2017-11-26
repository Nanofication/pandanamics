from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/home.html') # location of html template