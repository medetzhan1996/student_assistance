from django.db.models.signals import post_save
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from accounts.models import USERTYPE_STUDENT, USERTYPE_EXPERT
from .models import Message


@receiver(post_save, sender=Message)
def create_message(sender, instance, created, **kwargs):
    from_user = instance.from_user
    content_object = instance.content_object
    if from_user.role == USERTYPE_STUDENT:
        user = content_object.expert
    elif from_user.role == USERTYPE_EXPERT:
        user = content_object.demand.student
    channel_layer = get_channel_layer()
    data = {
        'id': instance.id,
        'type': 'notification',
        'demand_distribution_id': content_object.id,
        'demand_id': content_object.demand.id,
        'from_user': user.email
    }
    group_manager = 'notification_%s' % user.id
    async_to_sync(channel_layer.group_send)(
        group_manager, data)
