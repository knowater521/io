from django.contrib import admin
from models import Article, Category, Tag, Config
from adminfiles.admin import FilePickerAdmin

admin.site.register(Category)
admin.site.register(Tag)

class PostAdmin(FilePickerAdmin):
	adminfiles_fields = ('text',)

admin.site.register(Article, PostAdmin)
admin.site.register(Config, PostAdmin)

