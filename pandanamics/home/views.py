from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/home.html') # location of html template

def contact(request):
    return render(request, 'home/basic.html',
                  {'content':['If you would like to contact me, please email me',
                              'emailplaceholder@gmail.com']})