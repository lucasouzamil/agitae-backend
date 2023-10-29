from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .api.serializers import EventSerializer
from django.http import Http404, HttpResponse

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
        if events.exists():
            serialized_events = EventSerializer(events, many=True)
            return Response(serialized_events.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
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
        Event.objects.filter(id=event_id).delete()
        return HttpResponse(status=204)
    
    serialized_event = EventSerializer(event)
    return Response(serialized_event.data)