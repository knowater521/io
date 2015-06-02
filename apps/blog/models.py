# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Count, Max
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
   
    def CalFontSizeOfTag(self):
        min_font_size = 11
        max_font_size = 35
        tag_ref_num = self.GetArticleNum()
        # query blog_article_tag table
        # select max(tag_ref_num) from(select count(*) as tag_ref_num from blog_article_tag group by tag_id) as max_ref_num;
        max_tag_num = Article.tag.through.objects.values('tag_id').annotate(tag_ref_num=Count('*')).aggregate(max_ref_num=Max('tag_ref_num'))['max_ref_num']
        if max_tag_num <= 0:
            tag_ref_num = 0
        return min_font_size + tag_ref_num * (max_font_size - min_font_size) / max_tag_num

    def GetAbsoluteURL(self):
        return reverse('tag_home', kwargs={'slug':self.slug})

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128, default='anonymous')
    create_date = models.DateTimeField(auto_now_add=False)
    modify_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    text = MarkdownField(null=True)
    is_publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = '文章'

    def __unicode__(self):
        return self.title

    def GetTags(self):
        # get all Tag objects for this Article.
        return Article.objects.get(id=self.id).tag.all()

    def GetCategory(self):
        return Article.objects.get(id=self.id).category

class Config(models.Model):
    title = models.CharField(max_length=255)
    text = MarkdownField(null=True)

    def __unicode__(self):
        return self.title
