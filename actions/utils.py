import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def create_action(user, verb, target=None):
    # проверить любое подобное действие, сделанное в последнюю минуту
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(
        user_id=user.id, verb=verb, created__gte=last_minute
    )
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
                                             target_ct=target_ct,
                                             target_id=target.id)
    if not similar_actions:
        # существующие действия не найдены
        action = Action(user=user, verb=verb, target=target)
        action.save()
        actions_count = Action.objects.filter(user=user.id).count()
        channel_layer = get_channel_layer()
        data = {
                'verb': action.verb,
                'actions_count': actions_count,
                'type': 'action_notification'
            }
        group_manager = 'notification_%s' % user.id
        async_to_sync(channel_layer.group_send)(
            group_manager, data)
        return True
    return False
