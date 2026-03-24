from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'content')
    list_filter = ('published',)