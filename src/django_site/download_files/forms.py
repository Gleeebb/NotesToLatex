# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from .models import File, User
from django.contrib.auth.forms import UserCreationForm, UsernameField




class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="",
    )

    password2 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="Повторите пароль",
    )

    username = forms.CharField(
        help_text="Имя пользователя должно содержать только английские буквы.",
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}


class LoginForm(forms.ModelForm):
    password = forms.CharField(
       label=_("Password"),
       strip=False,
       widget=forms.PasswordInput,
       help_text="",
    )
    class Meta:
        model = User
        fields = ['email', 'password']



