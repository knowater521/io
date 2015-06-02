from django.contrib import admin
from models import Article, Category, Tag

from adminfiles.admin import FilePickerAdmin

#admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)


class PostAdmin(FilePickerAdmin):
	adminfiles_fields = ('text',)

admin.site.register(Article, PostAdmin)
