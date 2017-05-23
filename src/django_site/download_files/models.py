# coding=utf-8
from django.contrib.auth.models import User as BaseUser
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from pytesseract import *
from PIL import Image
# from .forms import CreateUserForm


class User(BaseUser):

    def saveChanges(self, data):
        self.last_name = (data['last_name'])
        self.first_name = (data['first_name'])
        self.email = (data['email'])
        self.save()


class File(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='')
    file_out = models.FileField(upload_to='text', default=None)

    def searchText(self, local='ru'):
        if len(self.file_out.name) <= 1:   # Дикий костыль
            im = Image.open(settings.BASE_DIR + self.file.url)
            string = image_to_string(im, lang=local)
            self.file_out.save(self.file.name, ContentFile(string))
            return string
        f = open(settings.BASE_DIR + self.file_out.url, 'r')
        return f.read()

    def saveChanges(self, new_string):
        f = open(settings.BASE_DIR + self.file_out.url, 'w')
        f.write(new_string)
        f.close()


class ProfilePhoto(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='')
    date = models.DateTimeField(auto_now_add=True, blank=True)
