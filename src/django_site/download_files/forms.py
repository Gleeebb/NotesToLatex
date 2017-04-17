from django import forms
from .models import File, User
from django.views.generic import FormView


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['user', 'file']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

