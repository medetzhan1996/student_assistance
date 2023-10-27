from django.db.models.signals import post_save
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Demand, DemandDistribution
from employment_portfolio.models import Portfolio
from actions.utils import create_action


@receiver(post_save, sender=Demand)
def create_demand(sender, instance, created, **kwargs):
    if instance.is_distribution and created:
        portfolios = Portfolio.objects.filter(type_tasks=instance.type_task).all()
        for portfolio in portfolios:
            demand_distribution = DemandDistribution.objects.create(
                expert=portfolio.user,
                demand=instance
            )
            create_action(portfolio.user, 'Поступило новое задание!', demand_distribution)
            channel_layer = get_channel_layer()
            data = {
                'demand_distribution': demand_distribution.id,
                'type': 'notification'
            }
            group_manager = 'notification_%s' % demand_distribution.expert.id
            async_to_sync(channel_layer.group_send)(
                group_manager, data)
    else:
        pass
