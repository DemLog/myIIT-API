from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import *
from .permission import IsAuthorUserOrAdmin
from .models import Event


class EventDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_serializer_class(self):
        user = self.request.user
        if user.is_staff:
            return EventDetailAdminSerializer
        return EventDetailSerializer


class EventCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventUpdateSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EventUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsAuthorUserOrAdmin)
    queryset = Event.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_serializer_class(self):
        user = self.request.user
        if user.is_staff:
            return EventResolveSerializer
        return EventUpdateSerializer
