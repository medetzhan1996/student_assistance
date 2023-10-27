from django import forms

from .models import CallBack


class CallBackForm(forms.ModelForm):

    class Meta:
        model = CallBack
        fields = ['phone_number', 'first_name']
