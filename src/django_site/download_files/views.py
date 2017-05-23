# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.base import View
from forms import FileForm, CreateUserForm, AuthenticationForm, TextInput, \
                  ChangeProfile, PasswordChangeForm, ProfilePhotoForm
from models import File, User, ProfilePhoto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.utils.datastructures import MultiValueDictKeyError



# Представление стартовой страницы.
class Index(View):

    def get(self, request):
        text = r'hello'
        return render(request, 'download_files/index.html',
                      {'nbar': 'home'})


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

    @method_decorator(login_required(redirect_field_name='index'))
    def get(self, request, img_id):
        img_id = int(img_id)
        img = File.objects.get(id=img_id)
        form = TextInput(initial={'content': img.searchText()})
        return render(request, 'download_files/editor.html',
                      {'img': img, 'form': form})

    @method_decorator(login_required(redirect_field_name='index'))
    def post(self, request, img_id):
        img_id = int(img_id)
        img = File.objects.get(id=img_id)
        form = TextInput(request.POST or None)
        if form.is_valid():
            data = form.save()
            img.saveChanges(data)
        return render(request, 'download_files/editor.html',
                      {'img': img, 'form': form})


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
            user = User.objects.get(id = request.user.id)
            newform.user = user
            newform.save()
            return redirect('myfiles')
        text = 'error'
        return render(request, 'download_files/index.html',
                      {'text': text})


class Profile(View):

    @method_decorator(login_required(redirect_field_name='index'))
    def get(self, request, type):
        try:
            img = ProfilePhoto.objects.filter(user = request.user).order_by('date').first()
        except ProfilePhoto.DoesNotExist:
            img = None
        form_photo = ProfilePhotoForm()
        if type == "password":
            form = PasswordChangeForm(request.user)
        if type == "data":
            this_user = User.objects.get(id = request.user.id)
            initial = {'first_name': this_user.first_name,
                'last_name': this_user.last_name,
                'email': this_user.email
            }
            form = ChangeProfile(initial)
        return render(request, 'download_files/profile.html',
                      {'nbar': 'prf',
                       'form': form,
                       'text': "",
                       'type': type,
                       'img': img,
                       'form_photo': form_photo})

    @method_decorator(login_required(redirect_field_name='index'))
    def post(self, request, type):

        if type == "password":
            form = PasswordChangeForm(request.user, request.POST)
        if type == "data":
            this_user = User.objects.get(id = request.user.id)
            form = ChangeProfile(request.POST or None)
        if form.is_valid():
            if type == "data":
                this_user.saveChanges(form.cleanData())
            if type == "password":
                user = form.save()
                update_session_auth_hash(request, user)

        form = ProfilePhotoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            user = User.objects.get(id = request.user.id)
            newform.user = user
            newform.save()
        return redirect('/profile/data')


class Contacts(View):

    def get(self, request):
        return render(request, 'download_files/contacts.html',
                      {'nbar': 'cnt'})
