from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    series = models.ForeignKey('home.Topic', related_name='Topic', null=True)

    def __str__(self):
        return self.title