from django.db import models
from django.conf import settings
from directory.models import TypeTask
from django.db.models import Q


class Demand(models.Model):
    """Список поступивщих задач"""
    DIPLOM_TYPE_CHOICES = (
        (1, 'Общая'),
        (2, 'Теория'),
        (3, 'Практика')
    )
    LANG_CHOICES = (
        (1, 'Казахский'),
        (2, 'Русский'),
        (3, 'Английский')
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_task = models.ForeignKey(TypeTask, on_delete=models.CASCADE)
    diplom_type = models.PositiveSmallIntegerField(
        choices=DIPLOM_TYPE_CHOICES, default=1)
    language = models.PositiveSmallIntegerField(
        choices=LANG_CHOICES, default=1)
    subject = models.CharField(max_length=250)
    deadline = models.DateField()
    comment = models.TextField()
    is_archive = models.BooleanField(default=False)
    is_distribution = models.BooleanField(default=True)
    is_expert_selected = models.BooleanField(default=False)

    def get_responsive_distributions(self):
        return self.demanddistribution_set.filter(status__in=[2, 3, 4]).all()

    def get_count_responsive_distributions(self):
        return self.demanddistribution_set.filter(status=2).count()


class DemandFile(models.Model):
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    file = models.FileField(upload_to='demand_files')
    date = models.DateField(auto_now_add=True)


class DemandCompletedFile(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    file = models.FileField(upload_to='demand_completed_files')
    date = models.DateField(auto_now_add=True)


class DemandDistribution(models.Model):
    """ Распределение задач по экспертам """
    STATUS_TYPE_CHOICES = (
        (1, 'Ожидание'),
        (2, 'Отклик'),
        (3, 'Ожидание оплаты'),
        (4, 'Заказ принят'),
        (5, 'Заказ оплачено'),
    )

    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_TYPE_CHOICES, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    prepayment = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    is_expert_selected = models.BooleanField(default=False)

