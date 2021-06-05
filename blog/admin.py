from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    list_filter = ('status', 'category')
    search_fields = ('title', 'body')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
