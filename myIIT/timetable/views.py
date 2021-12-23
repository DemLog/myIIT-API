from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Lecturer

START_DAY = date(2021, 8, 30)  # день начала учебы


def is_even_week(day_now):
    number_week = abs(day_now - START_DAY).days // 7 + 1
    return not (number_week % 2)


def get_day_week(day_now):
    return day_now.day // 7 + 1


class LecturerDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Lecturer.objects.all()
    serializer_class = LecturerDetailSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj


class LecturerListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Lecturer.objects.all()
    serializer_class = LecturerDetailSerializer


class TimeScheduleListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TimeSchedule.objects.all()
    serializer_class = TimeScheduleSerializer


class LessonScheduleDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LessonScheduleDetailSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        group = self.request.user.get_study_group
        return LessonSchedule.objects.filter(groups=group)


class LessonScheduleListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LessonScheduleListSerializer

    def get_queryset(self):
        group = self.request.user.get_study_group
        return LessonSchedule.objects.filter(groups=group)


class TimeTableTodayListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LessonScheduleDetailSerializer

    def get_queryset(self):
        group = self.request.user.get_study_group
        lessons = LessonSchedule.objects.filter(groups=group).order_by('time')
        number_week = 2 if is_even_week(date.today()) else 1
        day_week = LessonSchedule.CHOICES_WEEK[get_day_week(date.today()) - 1][0]
        return lessons.filter(number_week=number_week).filter(day_week=day_week)


class TimeTableWeekListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LessonScheduleListSerializer

    def get_queryset(self):
        group = self.request.user.get_study_group
        lessons = LessonSchedule.objects.filter(groups=group).order_by('day_week', 'time')
        number_week = 2 if is_even_week(date.today()) else 1
        return lessons.filter(number_week=number_week)
