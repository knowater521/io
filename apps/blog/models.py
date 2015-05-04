from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    #tags = models.ManyToManyField()
    author = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    content = models.TextField()
    is_publish = models.BooleanField(default=True)



    def __str__(self):
        return  self.headline