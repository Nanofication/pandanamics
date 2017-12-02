from django.db import models
from django.apps import apps

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.title
