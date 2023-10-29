from rest_framework import viewsets
from events.api import serializers
from events import models

class EventViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.EventSerializer
    queryset=models.Event.objects.all()