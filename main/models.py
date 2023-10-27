from django.db import models


class CallBack(models.Model):
    """ Обратный звонок """
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    