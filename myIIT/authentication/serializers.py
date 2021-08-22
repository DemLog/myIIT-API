from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User
from .moodle import MoodleAuth


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'email',
            'password',
            'token',
            'first_name',
            'last_name',
            'patronymic',
            'study_group',
            'direction',
            'is_admin'
        ]
        read_only_fields = ['token']

    def update(self, instance, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)

        if email is None or password is None:
            raise serializers.ValidationError(
                'Введите email и пароль!'
            )

        moodle = MoodleAuth(email, password)
        moodle_data = moodle.check_account()
        if 'error_message' in moodle_data:
            raise serializers.ValidationError(moodle_data['error_message'])

        for key, value in moodle_data.items():
            setattr(instance, key, value)

        instance.set_password(password)
        instance.save()

        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta(object):
        model = User
        fields = ['id', 'user_id', 'email', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, write_only=True)
    user_id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Не получен Email в запросе.'
            )
        if password is None:
            raise serializers.ValidationError(
                'Не получен пароль в запросе'
            )
        check_user = User.objects.get(email=email)
        if check_user is None:
            raise serializers.ValidationError(
                'Такого аккаунта нет в базе.'
            )

        user = authenticate(username=check_user.user_id, password=password)
        if user is None:
            raise serializers.ValidationError(
                'Произошла ошибка при запросе в базу. Повторите попытку'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Аккаунт деактивирован. Дальнейшие операции с ним недоступны'
            )

        return {
            'user_id': user.user_id,
            'token': user.token
        }


class LoginVKSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        try:
            user = User.objects.get(user_id=data['user_id'])
        except User.DoesNotExist:
            user = None

        if user is None:
            raise serializers.ValidationError(
                'Такого аккаунта нет в базе.'
            )

        return {
            'user_id': user.user_id,
            'token': user.token
        }
