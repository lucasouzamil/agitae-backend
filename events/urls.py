from django.urls import path
from . import views


from . import views

urlpatterns = [
    path('events/api/', views.api_events),
    path('events/api/<str:event_id>/', views.api_event),
    path('eventtypes/api/', views.api_eventtypes),
    path('eventtypes/api/<str:eventtype_id>/', views.api_eventtype),
]