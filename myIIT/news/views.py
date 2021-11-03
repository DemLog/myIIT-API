from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import *
from .models import Article, CategoryArticle


# создание новости
class ArticleCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ArticleDetailSerializer


# отображение всех новостей
class ArticlesListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()


# отображение статьи
class ArticleDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj


# отображение, обновление, удаление статьи
class ArticleEditView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj


# создание категории новости
class CategoryArticleCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = CategoryArticleDetailSerializer


# отображение всех категорий
class CategoriesArticleListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoriesArticleListSerializer
    queryset = CategoryArticle.objects.all()


# отображение категории
class CategoryArticleDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoryArticleDetailSerializer
    queryset = CategoryArticle.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj


# отображение, обновление, удаление категории
class CategoryArticleEditView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = CategoryArticleDetailSerializer
    queryset = CategoryArticle.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj
