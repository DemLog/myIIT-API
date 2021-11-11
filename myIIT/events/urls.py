from django.urls import path

from .views import EventDetailView, EventCreateView, EventUpdateView

app_name = 'events'
urlpatterns = [
    path('getEvent', EventDetailView.as_view()),  # Для пользователя и особых групп
    path('createEvent', EventCreateView.as_view()),
    path('editEvent', EventUpdateView.as_view()),  # Для пользователя и особых групп
]
