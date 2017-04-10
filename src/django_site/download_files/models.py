# coding=utf-8
from django.db import models


# Пока без регистрации пользователей, человек пишет ник
# под которым и будут хранится его данные в базе данных
class User(models.Model):
    user_name = models.CharField(max_length=40, unique=True)

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='files/')
