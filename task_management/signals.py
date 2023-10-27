from django.db.models.signals import post_save
from django.dispatch import receiver


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
            
    else:
        pass
