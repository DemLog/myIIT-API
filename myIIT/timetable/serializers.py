from rest_framework import serializers
from .models import Lecturer, TimeSchedule, Subject, LessonSchedule


class LecturerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('last_name', 'first_name', 'patronymic', 'position')


class LecturersListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_lecture_name')

    class Meta:
        model = Lecturer
        read_only_fields = ('full_name', 'position')


class TimeScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSchedule
        fields = ('number', 'start_time', 'end_time')


class SubjectListSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Subject
        fields = ('title', 'type')


class LessonScheduleDetailSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.__str__', read_only=True)
    lecture = serializers.CharField(source='lecture.get_lecture', read_only=True)
    cabinet = serializers.CharField(source='cabinet.__str__', read_only=True)
    time = TimeScheduleSerializer()
    day_week = serializers.IntegerField(source='get_day_week', read_only=True)

    class Meta:
        model = LessonSchedule
        fields = ('subject', 'number_week', 'lecture', 'cabinet', 'time', 'day_week', 'start_week', 'end_week')


class LessonScheduleListSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.__str__', read_only=True)
    lecture = serializers.CharField(source='lecture.get_lecture_name', read_only=True)
    cabinet = serializers.CharField(source='cabinet.__str__', read_only=True)
    time = TimeScheduleSerializer()
    day_week = serializers.IntegerField(source='get_day_week', read_only=True)

    class Meta:
        model = LessonSchedule
        fields = ('subject', 'lecture', 'cabinet', 'time', 'day_week')
