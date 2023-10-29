from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from events.api import viewsets as eventsviewsets

route = routers.DefaultRouter()

route.register(r'events/api/interface',eventsviewsets.EventViewSet, basename='Events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
    path('', include('events.urls')),
]
