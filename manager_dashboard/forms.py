from django import forms
from crispy_forms.helper import FormHelper
from accounts.models import CustomUser
from task_management.models import Demand, DemandDistribution


class DemandManagerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = CustomUser.objects.filter(role=1).order_by("-id")
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.template = 'task_management/demand/form_inner.html'

    class Meta:
        model = Demand
        fields = ['type_task', 'student', 'subject', 'deadline', 
        'comment', 'diplom_type', 'language', 'is_distribution']
        exclude = ['is_expert_selected']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'deadline': forms.TextInput(attrs={'type': 'date'})
        }
        labels = {
            'type_task': 'Тип задачи',
            'subject': 'Предмет',
            'deadline': 'Срок',
            'comment': 'Комментарий'
        }

class DemandDistributionManagerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.template = 'task_management/demand_distribution/form_inner.html'
        self.fields['expert'].queryset = CustomUser.objects.filter(role=2)


    class Meta:
        model = DemandDistribution
        fields = ['status', 'price', 'comment', 'phone_number', 'expert', 'prepayment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'status': 'Статус',
            'price': 'Введти предлогаемую цену',
            'comment': 'Введите комментарий',
            'phone_number': 'Введите ваш телефон номер'
        }