from django import template
from apps.blog.models import Category, Tag

register = template.Library()

@register.inclusion_tag('categories_list.html', takes_context=True)
def GetCategories(context):
	categories = Category.objects.all()
	return {'categories':categories}

@register.inclusion_tag('tags_cloud.html', takes_context=True)
def GetTags(context):
	tags = Tag.objects.all()
	return {'tags':tags}
	


