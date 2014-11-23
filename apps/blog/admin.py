from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_timestamp'

admin.site.register(Article, ArticleAdmin)