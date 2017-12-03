from django.db import models

# Create your models here.

class Post(models.Model):
    display_title = models.CharField(max_length=140, null=True) # What users will see
    title = models.CharField(max_length=140) # What database and code will see
    body = models.TextField()
    date = models.DateTimeField()
    topic = models.ForeignKey('home.Topic', related_name='Topic', null=True)

    def __str__(self):
        return "DISPLAY TITLE: %s       |     DB_TITLE: %s" % (self.display_title, self.title)