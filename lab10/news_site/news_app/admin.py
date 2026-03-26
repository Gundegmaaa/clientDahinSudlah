from django.contrib import admin

from .models import Category, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at']
