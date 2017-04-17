# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Пока без регистрации пользователей, человек пишет ник
# под которым и будут хранится его данные в базе данных
#


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='files/')
