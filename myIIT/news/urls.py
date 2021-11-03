from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('editArticle', ArticleEditView.as_view()),
    path('deleteArticle', ArticleEditView.as_view()),
    path('createArticle', ArticleCreateView.as_view()),
    path('getArticle', ArticleDetailView.as_view()),
    path('getListArticle', ArticlesListView.as_view()),
    path('editCategory', CategoryArticleEditView.as_view()),
    path('deleteCategory', CategoryArticleEditView.as_view()),
    path('createCategory', CategoryArticleCreateView.as_view()),
    path('getCategory', CategoryArticleDetailView.as_view()),
    path('getListCategory', CategoriesArticleListView.as_view()),
]
