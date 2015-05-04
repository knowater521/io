from django.db import models
import datetime

class Article(models.Model):
    title = models.CharField(max_length=200)
    #tags = models.ManyToManyField()
    author = models.CharField(max_length=100, default='anonymous')
    create_date = models.DateField(auto_now_add=True, default=datetime.datetime.now())
    modify_date = models.DateField(auto_now=True, default=datetime.datetime.now())
    content = models.TextField(default='')
    is_publish = models.BooleanField(default=True)


    def __str__(self):
        return  self.content