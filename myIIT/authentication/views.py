from rest_framework import status
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from collections import OrderedDict
from base64 import b64encode
from hashlib import sha256
from hmac import HMAC
from django.conf import settings
from urllib.parse import urlencode

from .serializers import UserSerializer, RegistrationSerializer, LoginSerializer
from .models import User


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        vk_id = kwargs.get('vk_id', None)
        if vk_id is not None:
            try:
                user = User.objects.get(vk_id=vk_id)
            except User.DoesNotExist:
                return Response({"error": "Пользователя с таким ID не существует!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersRetrieveListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()


# class UserUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = (IsAuthenticated, IsAdminUser)
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#     def update(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = LoginSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request):
        if not check_vk_valid(request):
            return Response({"error": "Не правильный ключ VK!"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'login': 'None',
            'password': 'None'
        }
        serializer = LoginSerializer(data=data, context={'vk_id': int(request.GET['vk_user_id'])})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def check_vk_valid(request):
    if not ('sign' in request.GET):
        return False
    vk_subset = OrderedDict(sorted(x for x in request.GET.items() if x[0][:3] == "vk_"))
    hash_code = b64encode(
        HMAC(settings.SECRET_KEY_VK_APP.encode(), urlencode(vk_subset, doseq=True).encode(), sha256).digest()
    )
    decoded_hash_code = hash_code.decode('utf-8')[:-1].replace('+', '-').replace('/', '_')
    if not (request.GET["sign"] == decoded_hash_code):
        return False
    return True
