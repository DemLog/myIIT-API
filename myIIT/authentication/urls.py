from django.urls import path

from .views import CreateAPIView, LoginAPIView

app_name = 'authentication'
urlpatterns = [
    path('create/', CreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
