from django.db import models
import datetime

class Article(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
    update_timestamp = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
    title = models.CharField(max_length=64, default='title')
    content = models.TextField(default='content')
    is_published = models.BooleanField(db_index=True, default=True)

    def __unicode__(self):
        return u"[%s](create: %s update: %s)"%(self.title, self.create_timestamp, self.update_timestamp)