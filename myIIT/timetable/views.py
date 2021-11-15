from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Lecturer


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
