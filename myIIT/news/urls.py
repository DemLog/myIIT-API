from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'news'
urlpatterns = [
    path('article/create/', ArticleCreateView.as_view()),
    path('article/', ArticlesListView.as_view()),
    path('article/category/create/', CategoryArticleCreateView.as_view()),
    path('article/category/', CategoriesArticleListView.as_view()),
]
