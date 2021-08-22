from rest_framework import generics
from .serializers import *
from .models import Article, CategoryArticle


# создание новости
class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer


# отображение всех новостей
class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()


# редактирование, отображение, удаление статьи
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()


# создание категории новости
class CategoryArticleCreateView(generics.CreateAPIView):
    serializer_class = CategoryArticleDetailSerializer

# отображение всех категорий
class CategoriesArticleListView(generics.ListAPIView):
    serializer_class = CategoriesArticleListSerializer
    queryset = CategoryArticle.objects.all()

# редактирование, отображение, удаление категории
class CategoryArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryArticleDetailSerializer
    queryset = CategoryArticle.objects.all()
