from rest_framework import serializers
from .models import Event

from authentication.models import User


class UserEventSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ('id', 'vk_id', 'username', 'study_group')


class EventDetailSerializer(serializers.ModelSerializer):
    author = UserEventSerializer(read_only=True)
    votes = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'author', 'votes', 'date_create')


class EventDetailAdminSerializer(serializers.ModelSerializer):
    author = UserEventSerializer(read_only=True)
    votes = UserEventSerializer(read_only=True, many=True)
    votes_count = serializers.IntegerField(source='votes.count', read_only=True)
    status_text = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'author', 'votes', 'votes_count', 'date_create', 'status',
                  'status_text', 'report')

    def get_status_text(self, obj):
        return obj.get_status_display()


class EventUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description')


class EventResolveSerializer(serializers.ModelSerializer):
    author = UserEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'status', 'report', 'author', 'date_create')
        read_only = ('id', 'author', 'date_create')
