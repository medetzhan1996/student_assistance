import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _type = text_data_json['type']
        recipient_room = self.room_group_name
        await self.channel_layer.group_send(
            recipient_room,
            {
                'type': _type,
                **text_data_json
            }
        )

    # receive message from room group
    async def chat_message(self, event):
        now = timezone.now()
        data = {
            **event,
            'datetime': now.isoformat()
        }
        await self.send(text_data=json.dumps(event))


class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.room_group_name = f'notification_{self.user.id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from room group
    async def notification(self, event):
        await self.send(text_data=json.dumps(event))


    async def action_notification(self, event):
        await self.send(text_data=json.dumps(event))

    async def chat_notification(self, event):
        await self.send(text_data=json.dumps(event))

