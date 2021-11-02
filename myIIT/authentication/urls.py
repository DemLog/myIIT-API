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
    path('getProfile', UserRetrieveAPIView.as_view()),
    path('getUser/<int:vk_id>', UserRetrieveAPIView.as_view()),
    # path('editUser/<int:vk_id>', UserUpdateAPIView.as_view()),
    path('getAllUser', UsersRetrieveListAPIView.as_view()),
    path('regUser', UserCreateAPIView.as_view()),
    path('loginUser', UserLoginAPIView.as_view()),
    
]
