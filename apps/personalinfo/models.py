from django.db import models
import datetime

class Me(models.Model):
	name = models.CharField(max_length=128, default='unknown')
	birthday = models.DateField(auto_now_add=False, default=datetime.datetime.now)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=64, default='Male', choices=GENDER_CHOICES)
	email = models.EmailField(max_length=64, default='example@iolala.com')
	qq = models.CharField(max_length=64, default='1234567890', verbose_name='QQ')

	class Meta:
		verbose_name_plural = 'ME'

	def __unicode__(self):
		return self.name