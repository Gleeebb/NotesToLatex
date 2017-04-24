# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from forms import FileForm, CreateUserForm, LoginForm
from django.views.generic.base import View
from django.contrib.auth import authenticate


# Представление стартовой страницы.
class Index(View):
    def get(self, request):
        text = r'hello'
        return render(request, 'download_files/index.html', {'text': text, 'nbar': 'home'})



# Представление страницы загрузки.
class Download(View):
    def post(self, request):
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    def get(self, request):
        form = FileForm()
        return render(request, 'download_files/download.html', {'form': form, 'nbar': 'dwn'})



# Представление страницы регистрации пользователей.
class Register(View):
    def post(self, request):
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            text = "Cпасибо за регистрацию!"
        else:
            text = r'Registration Error'
        return render(request, 'download_files/index.html', {'text': text})
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'download_files/registration.html', {'form_register': form, 'nbar': 'rgst'})

# Проблемы с непосредственно авторизацией.
class Login(View):
    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            print form.cleaned_data['email'], form.cleaned_data['password']
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    text = r"User is valid, active and authenticated"
                else:
                    text = r"The password is valid, but the account has been disabled!"
            else:
                text = r'ERROR'
        else:
            text = r'Log in error'
        return render(request, 'download_files/index.html', {'text': text})
    def get(self, request):
        form = LoginForm()
        return render(request, 'download_files/login.html', {'form': form, 'nbar': 'lgn'})