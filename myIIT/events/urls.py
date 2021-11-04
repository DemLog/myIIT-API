from django.urls import path

from .views import EventDetailView, EventDetailAdminView

app_name = 'events'
urlpatterns = [
    path('getEvent', EventDetailView.as_view()),
    path('getEventFull', EventDetailAdminView.as_view()),
    path('deleteEvent', EventDetailAdminView.as_view()),
    path('editEvent', EventDetailAdminView.as_view()),
]