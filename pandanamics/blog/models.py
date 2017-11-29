from django.db import models

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    series = models.ForeignKey(Topic, related_name='Topic', null=True)

    def __str__(self):
        return self.title