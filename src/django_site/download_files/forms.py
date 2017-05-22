# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from .models import File, User
from tinymce import TinyMCE




class FileForm(forms.ModelForm):
    file = forms.ImageField(
        label = ("Добавить файл"),
        help_text = "",

    )

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
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2')
        field_classes = {'username': UsernameField}


class AuthenticationForm(forms.Form):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )



class TextInput(forms.Form):
    content = forms.CharField(widget=TinyMCE(mce_attrs={}))

    def save(self):
        return self.cleaned_data['content'].encode('utf-8')
