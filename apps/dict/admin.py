from django.contrib import admin
from .models import Dict

class DictAdmin(admin.ModelAdmin):
    alphabet_filter = 'english'
    DEFAULT_ALPHABET = u''

admin.site.register(Dict, DictAdmin)
