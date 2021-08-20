from django.urls import path

from .views import CreateAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/', CreateAPIView.as_view()),
]