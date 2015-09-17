from django import template
from apps.blog.models import Category, Tag
from random import shuffle

register = template.Library()

@register.inclusion_tag('blog/categories_list.html', takes_context=True)
def GetCategories(context):
	categories = Category.objects.all()
	return {'categories':categories}

@register.inclusion_tag('blog/tags_cloud.html', takes_context=True)
def GetTags(context):
	tags = Tag.objects.all().order_by('?')
	return {'tags':tags}
	


