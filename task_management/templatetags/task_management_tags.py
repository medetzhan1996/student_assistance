from django.db.models import Count
from django import template
from ..models import DemandDistribution
from directory.models import Subject

register = template.Library()


@register.simple_tag
def get_selected_demand_distribution(query, status):
    return DemandDistribution.objects.filter(demand=query, status=status).first()

@register.simple_tag
def get_subject_list():
    return Subject.objects.all()



