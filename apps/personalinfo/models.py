import datetime
from django.db import models
from storage import OverwriteStorage

class MyInfo(models.Model):
	name = models.CharField(max_length=128, default='unknown')
	birthday = models.DateField(auto_now_add=False, default=datetime.datetime.now)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=64, default='Male', choices=GENDER_CHOICES)
	email = models.EmailField(max_length=64, default='example@iolala.com')
	qq = models.CharField(max_length=64, default='1234567890', verbose_name='QQ')
	weibo = models.CharField(max_length=255, default='http://weibo.com', null=True, verbose_name='Weibo')
	github = models.CharField(max_length=255, default='https://github.com', null=True, verbose_name='GitHub')
	avator = models.ImageField(upload_to='avator/', storage=OverwriteStorage(), null=True)
	is_show_qq = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'ME'

	def __unicode__(self):
		return self.name

class MyWorks(models.Model):
	order_number = models.IntegerField(default=1)
	name = models.CharField(max_length=128, default='io')
	image_link = models.CharField(max_length=256, default='xx')
	homepage = models.CharField(max_length=256, default='www.iolala.com')
	desc = models.TextField(null=True, default='This is a ...')

	class Meta:
		verbose_name_plural = 'Works'

	def __unicode__(self):
		return self.name

