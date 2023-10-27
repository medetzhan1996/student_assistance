from django import template
from accounts.models import CustomUser
from task_management.models import DemandDistribution

register = template.Library()

@register.simple_tag
def get_user_role_list(role):
    if role==1:
        return CustomUser.objects.filter(role=role).order_by("-id")
    if role==2:
        return CustomUser.objects.filter(role=role)

@register.simple_tag
def get_selected_demand_distribution(query):
    return DemandDistribution.objects.get(demand=query, is_expert_selected=True)



