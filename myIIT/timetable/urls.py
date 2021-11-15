from django.urls import path
from .views import *

app_name = 'timetable'
urlpatterns = [
    path('getLecturer', LecturerDetailView.as_view()),
    path('getAllLecturer', LecturerListView.as_view()),
    path('getTimeSchedule', TimeScheduleListView.as_view()),
    path('getLesson', LessonScheduleDetailView.as_view()),
    path('getAllLesson', LessonScheduleListView.as_view()),
]
