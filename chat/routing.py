from django.urls import re_path
from .import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\d+)/room/', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/notification/room/(?P<demand_distribution_id>\d+)/', consumers.NotificationConsumer.as_asgi()),
]

