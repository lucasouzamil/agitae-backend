from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event, EventType, EventSubType
from .api.serializers import EventSerializer, EventTypeSerializer, EventSubTypeSerializer
from django.http import Http404, HttpResponse
import os
from datetime import date
from django.utils.timezone import now

@api_view(['GET', 'POST'])
def api_events(request):
    if request.method == 'POST':
        new_event_data = request.data
        serializer = EventSerializer(data=new_event_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        events = Event.objects.all()
        outdated_events = [event for event in events if event.date < date.today()]
        if outdated_events:
            for event in outdated_events:
                delete_event(event.id)
            events = Event.objects.all()
            serialized_events = EventSerializer(events, many=True)
            return Response(serialized_events.data)
        else:
            serialized_events = EventSerializer(events, many=True)
            return Response(serialized_events.data)
        
    if request.method == 'DELETE':
        events = Event.objects.all()
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'POST', 'DELETE'])
def api_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        raise Http404()

    if request.method == 'DELETE':
        delete_event(event_id)
        return HttpResponse(status=204)
    
    serialized_event = EventSerializer(event)
    return Response(serialized_event.data)

@api_view(['GET', 'POST'])
def api_eventtypes(request):
    if request.method == 'POST':
        new_eventtype_data = request.data
        serializer = EventTypeSerializer(data=new_eventtype_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        eventtypes = EventType.objects.all()
        serialized_eventtypes = EventTypeSerializer(eventtypes, many=True)
        return Response(serialized_eventtypes.data)
        
    if request.method == 'DELETE':
        eventtypes = EventType.objects.all()
        eventtypes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def api_eventtype(request, eventtype_id):
    try:
        eventtype = EventType.objects.get(id=eventtype_id)
    except EventType.DoesNotExist:
        raise Http404()

    if request.method == 'DELETE':
        eventtype = EventType.objects.get(id=eventtype_id)
        eventtype.delete()
        return HttpResponse(status=204)
    
    serialized_eventype = EventTypeSerializer(eventtype)
    return Response(serialized_eventype.data)

@api_view(['GET', 'POST'])
def api_eventsubtypes(request):
    if request.method == 'POST':
        new_eventsubtype_data = request.data
        serializer = EventSubTypeSerializer(data=new_eventsubtype_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        eventsubtypes = EventSubType.objects.all()
        serialized_eventsubtypes = EventSubTypeSerializer(eventsubtypes, many=True)
        return Response(serialized_eventsubtypes.data)
        
    if request.method == 'DELETE':
        eventsubtypes = EventSubType.objects.all()
        eventsubtypes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def api_eventsubtype(request, eventsubtype_id):
    try:
        eventsubtype = EventSubType.objects.get(id=eventsubtype_id)
    except EventSubType.DoesNotExist:
        raise Http404()

    if request.method == 'DELETE':
        eventsubtype = EventSubType.objects.get(id=eventsubtype_id)
        eventsubtype.delete()
        return HttpResponse(status=204)
    
    serialized_eventsubtype = EventSubTypeSerializer(eventsubtype)
    return Response(serialized_eventsubtype.data)

def delete_event(event_id):
    try:
        event = Event.objects.get(id=event_id)
        img_name=event.image.name
        if len(img_name.split(f'{str(event.id)}')) > 1:
            media_path = os.path.join(os.getcwd(), 'media', img_name)
            os.remove(media_path)
        event.delete()
    except Event.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)