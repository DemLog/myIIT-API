from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from collections import OrderedDict
from base64 import b64encode
from hashlib import sha256
from hmac import HMAC
from django.conf import settings
from urllib.parse import urlencode

from .serializers import (
    RegistrationSerializer, LoginSerializer, UserSerializer, LoginVKSerializer
)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer_data, status=status.HTTP_200_OK)


class UserCreateAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = RegistrationSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        serializer = LoginSerializer(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLoginVKAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginVKSerializer

    def get(self, request):

        if not ('sign' in request.GET):
            return Response({"error": "Нет ключа подписи ВК."}, status=status.HTTP_400_BAD_REQUEST)

        vk_subset = OrderedDict(sorted(x for x in request.GET.items() if x[0][:3] == "vk_"))
        hash_code = b64encode(
            HMAC(settings.SECRET_KEY_VK_APP.encode(), urlencode(vk_subset, doseq=True).encode(), sha256).digest()
        )
        decoded_hash_code = hash_code.decode('utf-8')[:-1].replace('+', '-').replace('/', '_')
        if not (request.GET["sign"] == decoded_hash_code):
            return Response({"error": "ID не совпадает с ID из подписи."}, status=status.HTTP_403_FORBIDDEN)

        serializer = LoginVKSerializer(data={"user_id": int(request.GET['vk_user_id'])})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
