from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('editArticle/<int:pk>', ArticleEditView.as_view()),
    path('deleteArticle/<int:pk>', ArticleEditView.as_view()),
    path('createArticle/', ArticleCreateView.as_view()),
    path('getArticle/<int:pk>', ArticleDetailView.as_view()),
    path('getListArticle/', ArticlesListView.as_view()),
    path('editCategory/<int:pk>', CategoryArticleEditView.as_view()),
    path('deleteCategory/<int:pk>', CategoryArticleEditView.as_view()),
    path('createCategory/', CategoryArticleCreateView.as_view()),
    path('getCategory/<int:pk>', CategoryArticleDetailView.as_view()),
    path('getListCategory/', CategoriesArticleListView.as_view()),
]
