# coding=utf-8

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class UserBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None