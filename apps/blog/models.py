# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = '类型'

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = '标签'

    def __unicode__(self):
        return self.slug

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128, default='anonymous')
    create_date = models.DateField(auto_now_add=True, default=datetime.datetime.now())
    modify_date = models.DateField(auto_now=True, default=datetime.datetime.now())
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    content = models.TextField(default='')
    is_publish = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = '文章'

    def __unicode__(self):
        return self.title




