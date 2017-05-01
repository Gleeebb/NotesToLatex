# coding=utf-8
from django.contrib.auth.models import User, User
from django.db import models


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='files/')


class ProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='files/')