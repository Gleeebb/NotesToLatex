# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.base import View
from forms import FileForm, CreateUserForm, AuthenticationForm
from models import File
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Представление стартовой страницы.
class Index(View):

    def get(self, request):
        text = r'hello'
        return render(request, 'download_files/index.html',
                      {'text': request.user.id, 'nbar': 'home'})


# Представление страницы регистрации пользователей.
class Register(View):

    def post(self, request):
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            text = "Cпасибо за регистрацию!"
        else:
            text = r'Registration Error'
        return render(request, 'download_files/index.html',
                      {'text': text})

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'download_files/registration.html',
                      {'form_register': form, 'nbar': 'rgst'})


# Авторизация пользователя
class Login(View):

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    text = r"User is valid, active and authenticated"
                else:
                    text = r"The password is valid, but the account has\
                     been disabled!"
            else:
                text = r'ERROR'
        else:
            text = 'FORM is not valid'
        return render(request, 'download_files/index.html',
                      {'text':text})

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'download_files/login.html',
                      {'form': form, 'nbar': 'lgn'})


class Editor(View):

    def get(self, request, img_id):
        img_id = int(img_id)
        print img_id
        img = File.objects.get(id=img_id)
        # form = FlatPageForm()
        return render(request, 'download_files/editor.html',
                      {'img': img,})


class Logout(View):

    def get(self, request):
        logout(request)
        return render(request, 'download_files/index.html')



class MyFiles(View):

    @method_decorator(login_required(redirect_field_name='index'))
    def get(self, request):
        imgs = File.objects.filter(user = request.user)
        text = request.user
        form = FileForm()
        return render(request, 'download_files/files.html',
                      {'nbar': 'fls', 'text': text, 'imgs': imgs,
                       'form': form})

    @method_decorator(login_required(redirect_field_name='index'))
    def post(self, request):
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('index')
        text = 'error'
        return render(request, 'download_files/index.html',
                      {'text': text,})



