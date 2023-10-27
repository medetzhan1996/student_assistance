from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


USERTYPE_STUDENT = 1
USERTYPE_EXPERT = 2
USERTYPE_ADMIN = 3
USERTYPE_DEFAULT = USERTYPE_STUDENT


class CustomUser(AbstractUser):
    """Расширенная пользовательская модель"""
    USER_ROLE_CHOICES = (
        (USERTYPE_STUDENT, 'student'),
        (USERTYPE_EXPERT, 'expert'),
        (USERTYPE_ADMIN, 'admin'),
    )
    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, default=USERTYPE_STUDENT)
    email = models.CharField(_('email address'), unique=True, max_length=75)
    is_developer = models.BooleanField(default=False)

    class Meta(object):
        db_table = 'custom_user'

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
