from django.http import HttpResponse
from django.template import loader
from .models import Topic

def carousel(request):
    template = loader.get_template('home/carousel.html')
    context = {
        'topics' : Topic.objects.all()
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
