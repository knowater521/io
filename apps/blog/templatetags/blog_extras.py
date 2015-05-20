from django import template
from apps.blog.models import Category

register = template.Library()

@register.inclusion_tag('categories_list.html', takes_context=True)
def GetCategories(context):
	categories = Category.objects.all()
	return {'categories':categories}
	


