from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

from crispy_forms.helper import FormHelper

from .models import Profile

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.CharField(label='Телефон нөміріңізді енгізіңіз', max_length=75)
    role = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        del self.fields['password2']
        self.helper.form_tag = False

    class Meta:
        model = UserModel
        fields = ['email', 'role']
        exclude = ['username']

        labels = {
            'email': 'Телефон нөміріңізді енгізіңіз',
            'password1': 'Құпия сөзді ойлап табыңыз',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Бұл телефон нөмірі қазірдің өзінде бос емес.')
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        user.role = self.cleaned_data["role"]
        user.is_active = True
        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Телефон нөміріңізді енгізіңіз')