from django.contrib import admin
from apps.blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)