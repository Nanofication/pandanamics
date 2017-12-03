from django.db import models
from django.apps import apps
import re

class LowerCaseTitle(models.CharField):
    def to_python(self, value):
        title = re.sub(" ", "-", value.lower())
        return title

# Create your models here.
class Topic(models.Model):
    display_title = models.CharField(max_length=140, null=True) # What users will see
    title = models.CharField(max_length=140) # What the database will see
    date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return "DISPLAY TITLE: %s        |    DB_TITLE: %s"  % (self.display_title, self.title)
