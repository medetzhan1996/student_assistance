from django.db import models
from django.conf import settings
from directory.models import TypeTask, Subject


class Resume(models.Model):
    """ Резюме экспертов """
    WORK_TYPE_CHOICES = (
        (1, 'Подработка'),
        (2, 'Основной'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.CharField(max_length=180, null=True, blank=True)
    speciality = models.CharField(max_length=180, null=True, blank=True)
    university_year_end = models.DateField(null=True, blank=True)
    now_study_university = models.CharField(max_length=180, null=True, blank=True)
    now_study_speciality = models.CharField(max_length=180, null=True, blank=True)
    now_study_university_year_end = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=180, null=True, blank=True)
    current_city = models.CharField(max_length=180)
    date_birth = models.DateField()
    additional_education = models.CharField(max_length=180, null=True, blank=True)
    experience = models.BooleanField(default=False)
    work_type = models.PositiveSmallIntegerField(
        choices=WORK_TYPE_CHOICES, default=1)
    subjects = models.CharField(max_length=180)
    languages = models.CharField(max_length=180)
    social_profile_networks = models.CharField(max_length=180)
    support_document = models.FileField(upload_to='support_document/')


class Portfolio(models.Model):
    """Портфолио эксперта"""
    LANGUAGE_TYPE_CHOICES = (
        (1, 'Русский'),
        (2, 'Казахский'),
        (3, 'Английский'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_tasks = models.ManyToManyField(TypeTask)
    subjects = models.ManyToManyField(Subject)
    languages = models.PositiveSmallIntegerField(
        choices=LANGUAGE_TYPE_CHOICES, default=1)


class Comment(models.Model):
    """ Комментарий экспертам """
    RATING_TYPE_CHOICES = (
        (1, 'Очень плохо'),
        (2, 'Плохо'),
        (3, 'Удовлетворительно'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_TYPE_CHOICES, default=1)
    text = models.TextField()
    expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_expert')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_student')
    date = models.DateTimeField(auto_now_add=True)


class Claim(models.Model):
    """ Жалоба экспертам """
    text = models.TextField()
    expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='claim_expert')