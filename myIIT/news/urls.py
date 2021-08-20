from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'news'
urlpatterns = [
    path('article/create/', ArticleCreateView.as_view()),
    path('article/<int:pk>', ArticleDetailView.as_view()),
    path('article/', ArticlesListView.as_view()),
    path('category/create/', CategoryArticleCreateView.as_view()),
    path('category/<int:pk>', CategoryArticleDetailView.as_view()),
    path('category/', CategoriesArticleListView.as_view()),
]
