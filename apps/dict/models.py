from django.db import models
import datetime

class Dict(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
    update_timestamp = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
    english = models.CharField(max_length=128, default='english')
    chinese = models.CharField(max_length=128, default='chinese')

    def __unicode__(self):
        return u"%s - %s"%(self.english, self.chinese)
