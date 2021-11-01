from abc import ABC

from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        exclude = ('last_login', 'is_superuser', 'user_permissions',)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'vk_id', 'login', 'password', 'token',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    vk_id = serializers.IntegerField(read_only=True)
    token = serializers.CharField(max_length=256, read_only=True)

    def validate(self, data):
        login = data.get('login', None)
        password = data.get('password', None)
        vk_id = self.context.get('vk_id', None)

        if vk_id is not None:
            try:
                user = User.objects.get(vk_id=vk_id)
            except User.DoesNotExist:
                user = None
        else:
            if (login and password) is None:
                raise serializers.ValidationError(
                    'Не указан Логин Moodle или пароль!'
                )
            try:
                User.objects.get(login=login)
            except User.DoesNotExist:
                raise serializers.ValidationError(
                    'Такого аккаунта не существует в базе!'
                )
            user = authenticate(login=login, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Введен не правильно пароль, либо произошла ошибка на сервере!'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'Запрещен доступ к системе!'
            )

        return {
            'vk_id': user.vk_id,
            'token': user.token
        }
