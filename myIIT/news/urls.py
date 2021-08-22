from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('edit/<int:pk>', ArticleEditView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<int:pk>', ArticleDetailView.as_view()),
    path('', ArticlesListView.as_view()),
    path('category/edit/<int:pk>', CategoryArticleEditView.as_view()),
    path('category/create/', CategoryArticleCreateView.as_view()),
    path('category/<int:pk>', CategoryArticleDetailView.as_view()),
    path('category/', CategoriesArticleListView.as_view()),
]
