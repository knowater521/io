from django.db import models


# Create your models here.
class Article(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True,default=True)
    update_timestamp = models.DateTimeField(auto_now_add=True,default=True)
    title = models.CharField(max_length=64, default='title')
    content = models.TextField(default='content')
    is_published = models.BooleanField(db_index=True, default=True)

    def __unicode__(self):
        return u"[%s](%s)"%(self.title, self.create_timestamp)