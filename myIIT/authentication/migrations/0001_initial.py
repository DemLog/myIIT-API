# Generated by Django 3.2.6 on 2021-12-23 02:21

import authentication.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(max_length=128, unique=True, verbose_name='Логин Moodle')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль Moodle')),
                ('vk_id', models.IntegerField(unique=True, verbose_name='VK ID')),
                ('email', models.EmailField(max_length=256, verbose_name='Email Moodle')),
                ('first_name', models.CharField(blank=True, max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=64, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=64, verbose_name='Отчество')),
                ('country', models.CharField(blank=True, max_length=64, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='Город')),
                ('status', models.CharField(blank=True, max_length=16, verbose_name='Статус')),
                ('study_group', models.CharField(blank=True, max_length=16, verbose_name='Группа')),
                ('direction', models.CharField(blank=True, max_length=64, verbose_name='Направление обучения')),
                ('profile', models.CharField(blank=True, max_length=64, verbose_name='Профиль')),
                ('form_study', models.CharField(blank=True, max_length=16, verbose_name='Форма обучения')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный аккаунт')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', authentication.managers.UserManager()),
            ],
        ),
    ]
