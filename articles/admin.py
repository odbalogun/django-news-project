from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'body', 'author')

admin.site.register(Article)