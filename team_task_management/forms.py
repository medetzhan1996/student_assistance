from django import forms
from django.contrib.auth import get_user_model
from .models import Task, EmployeeDayRating
User = get_user_model()


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_developer=True)

    class Meta:
        model = Task
        fields = ['description', 'date', 'status', 'comment', 'user']
        exclude = ('send_by', )
        labels = {
            'description': 'Описание:',
            'date': 'Дата:',
            'status': 'Cтатус:',
            'comment': 'Комментарий:',
            'user': 'Выполняющий сотрудник'
        }
        widgets = {'date': forms.HiddenInput()}


class EmployeeDayRatingForm(forms.ModelForm):

    class Meta:
        model = EmployeeDayRating
        fields = ['recomend_rating', 'date', 'comment']
        labels = {
            'recomend_rating': 'Рекомендовать рейтинг:',
            'date': 'Дата:',
            'comment': 'Комментарий:'
        }
        widgets = {'date': forms.HiddenInput()}
