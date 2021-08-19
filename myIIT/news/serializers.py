from rest_framework import serializers
from .models import Article, CategoryArticle


class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'category', 'title', 'text', 'is_published')


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CategoryArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = '__all__'


class CategoriesArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = ('id', 'name', 'slug')
