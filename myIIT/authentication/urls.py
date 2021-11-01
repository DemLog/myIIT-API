from django.urls import path

from .views import (
    UserCreateAPIView,
    UserRetrieveAPIView,
    UserLoginAPIView,
    UsersRetrieveListAPIView,
    # UserUpdateAPIView
)

app_name = 'authentication'
urlpatterns = [
    path('user/', UserRetrieveAPIView.as_view()),
    path('user/<int:vk_id>', UserRetrieveAPIView.as_view()),
    # path('user/edit/<int:vk_id>', UserUpdateAPIView.as_view()),
    path('allusers/', UsersRetrieveListAPIView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    
]
