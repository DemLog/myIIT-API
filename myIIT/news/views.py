from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Article


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer


class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()


class CategoryArticleCreateView(generics.CreateAPIView):
    serializer_class = CategoryArticleDetailSerializer


class CategoriesArticleListView(generics.ListAPIView):
    serializer_class = CategoriesArticleListSerializer
    queryset = CategoryArticle.objects.all()


class CategoryArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryArticleDetailSerializer
    queryset = CategoryArticle.objects.all()
