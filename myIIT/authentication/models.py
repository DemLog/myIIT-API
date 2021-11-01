from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(verbose_name='Логин Moodle', unique=True, max_length=128)
    password = models.CharField(verbose_name='Пароль Moodle', max_length=128)
    vk_id = models.IntegerField(verbose_name='VK ID', unique=True)
    email = models.EmailField(verbose_name='Email Moodle', max_length=256)
    first_name = models.CharField(verbose_name='Имя', max_length=64, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64, blank=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=64, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=64, blank=True)
    city = models.CharField(verbose_name='Город', max_length=64, blank=True)
    status = models.CharField(verbose_name='Статус', max_length=16, blank=True)
    study_group = models.CharField(verbose_name='Группа', max_length=16, blank=True)
    direction = models.CharField(verbose_name='Направление обучения', max_length=64, blank=True)
    profile = models.CharField(verbose_name='Профиль', max_length=64, blank=True)
    form_study = models.CharField(verbose_name='Форма обучения', max_length=16, blank=True)
    date_joined = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Активный аккаунт', default=True)
    is_admin = models.BooleanField(verbose_name='Администратор', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['vk_id', 'password']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'vk_id': self.vk_id,
            'exp': datetime.utcnow() + timedelta(seconds=3600)
        }, settings.SECRET_KEY, algorithm="HS256")
        return token

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_admin
