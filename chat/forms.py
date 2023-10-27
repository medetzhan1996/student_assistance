from django import forms

from .models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['text', 'object_id']
        exclude = ('from_user', )
