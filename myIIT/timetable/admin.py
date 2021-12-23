from django.contrib import admin
from .models import *


@admin.register(LessonSchedule)
class LessonScheduleAdmin(admin.ModelAdmin):
    list_display = ['number_week', 'subject', 'cabinet']


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'position']


@admin.register(ClassCabinet)
class ClassCabinetAdmin(admin.ModelAdmin):
    list_display = ['title', 'building']


@admin.register(TimeSchedule)
class TimeScheduleAdmin(admin.ModelAdmin):
    list_display = ['number', 'get_time']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
