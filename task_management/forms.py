from django import forms

from crispy_forms.helper import FormHelper
from accounts.models import CustomUser
from .models import Demand, DemandDistribution, DemandFile, DemandCompletedFile


class DemandForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.template = 'task_management/demand/form_inner.html'

    class Meta:
        model = Demand
        fields = ['type_task', 'subject', 'deadline', 
        'comment']
        exclude = ['student', 'is_expert_selected']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'deadline': forms.TextInput(attrs={'type': 'date'})
        }
        labels = {
            'type_task': 'Тапсырма түрі',
            'subject': 'Тақырып',
            'deadline': 'Мерзімі',
            'comment': 'Сипаттама'
        }


class DemandDistributionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.template = 'task_management/demand_distribution/form_inner.html'


    class Meta:
        model = DemandDistribution
        fields = ['status', 'price', 'comment', 'phone_number', 'prepayment']
        exclude = ['expert']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'status': 'Статус',
            'price': 'Введти предлогаемую цену',
            'comment': 'Введите комментарий',
            'phone_number': 'Введите ваш телефон номер'
        }


class DemandFileForm(forms.ModelForm):
    pass

    class Meta:
        model = DemandFile
        fields = ['file']
        exclude = ['demand']


class DemandCompletedFileForm(forms.ModelForm):
    pass

    class Meta:
        model = DemandCompletedFile
        fields = ['file', 'demand']
