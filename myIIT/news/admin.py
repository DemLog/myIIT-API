from django.contrib import admin
from .models import Article, CategoryArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_published', 'is_published']


@admin.register(CategoryArticle)
class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ['name']
