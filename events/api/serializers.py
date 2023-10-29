from rest_framework import serializers
from events import models

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventType
        fields = '__all__'

class EventSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventSubType
        fields = '__all__'