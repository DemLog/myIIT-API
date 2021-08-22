from django.urls import path

from .views import (
    UserCreateAPIView, UserLoginAPIView, UserRetrieveUpdateAPIView
)

app_name = 'authentication'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
]
