from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .api.serializers import EventSerializer
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