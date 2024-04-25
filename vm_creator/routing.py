# routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ssh/', consumers.SSHConsumer.as_asgi()),
]
