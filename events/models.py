from django.db import models
from uuid import uuid4

def upload_event_iamge(instance,filename):
    return f"{instance.id}{filename}"


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, help_text="name")
    description = models.TextField(max_length=1000, help_text="description")
    url = models.URLField(help_text="url")
    date = models.DateField(help_text="date")
    time = models.TimeField(help_text="time")
    local_name = models.CharField(max_length=50, help_text="local name")
    state = models.CharField(max_length=50, help_text="state")
    city = models.CharField(max_length=50, help_text="city")
    neighborhood = models.CharField(max_length=50, help_text="neighborhood")
    street = models.CharField(max_length=50, help_text="street")
    number = models.IntegerField(help_text="number")
    image = models.ImageField(upload_to=upload_event_iamge, blank=True, null=True)

class EventSubType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name =  models.CharField(max_length=50, help_text="name")
    events =  models.ManyToManyField(Event, blank=True)

class EventType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name =  models.CharField(max_length=50, help_text="name")
    subtypes = models.ManyToManyField(EventSubType, blank=True)