# -*- coding: utf-8 -*-

from django.db import models
from django_markdown.models import MarkdownField
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = '类型'

    def __unicode__(self):
        return self.name

    def GetArticleNum(self):
	return Article.objects.filter(category=self).count()
    
    def GetAbsoluteURL(self):
        return reverse('category_home', kwargs={'slug':self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = '标签'

    def __unicode__(self):
        return self.name

    def GetArticleNum(self):
        return Article.objects.filter(tag=self).count()
    
    def GetAbsoluteURL(self):
        return reverse('tag_home', kwargs={'slug':self.slug})

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128, default='anonymous')
    create_date = models.DateField(auto_now_add=False)
    modify_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    text = MarkdownField(null=True)
    is_publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = '文章'

    def __unicode__(self):
        return self.title



class Test(models.Model):
    context = models.TextField(null=True) 
    def __unicode__(self):
        return self.context
