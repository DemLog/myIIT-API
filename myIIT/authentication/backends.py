import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    # authentication_header_prefix = 'Token'

    def authenticate(self, request):

        request.user = None
        auth_token = request.query_params.get('token', None)
        # auth_header_prefix = self.authentication_header_prefix.lower()

        if auth_token is None:
            return None

        return self._authenticate_credentials(auth_token)

    def _authenticate_credentials(self, token):

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        except Exception as error:
            raise exceptions.AuthenticationFailed('Ошибка аутентификации. Невозможно декодировать токен.')

        try:
            user = User.objects.get(vk_id=payload['vk_id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Пользователь соответствующий данному токену не найден.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Запрещен доступ к системе!')

        return (user, token)
