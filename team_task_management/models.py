import datetime
from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_TYPE_CHOICES = (
        (1, 'Не выполнен'),
        (2, 'Выполнен'),
        (3, 'Отказ'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_TYPE_CHOICES, default=1, verbose_name='Статус')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    send_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='send_by')


class EmployeeDayRating(models.Model):
    Rating_CHOICES = (
        (1, 'Не работал'),
        (2, 'Очень плохо'),
        (3, 'Плохо'),
        (4, 'Хорошо'),
        (5, 'отлично'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recomend_rating = models.PositiveSmallIntegerField(
        choices=Rating_CHOICES, default=1)
    date = models.DateField(default=datetime.date.today)
    rating = models.PositiveSmallIntegerField(
        choices=Rating_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    comment = models.TextField(blank=True)