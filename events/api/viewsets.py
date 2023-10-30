from rest_framework import viewsets
from events.api import serializers
from events import models

class EventViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.EventSerializer
    queryset=models.Event.objects.all()

class EventTypeViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.EventTypeSerializer
    queryset=models.EventType.objects.all()

class EventSubTypeViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.EventSubTypeSerializer
    queryset=models.EventSubType.objects.all()