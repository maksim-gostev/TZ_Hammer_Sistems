import time
from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from permission import UserAndRoleVerification
from users.serializers import UserSICSerializer, UserDetailSerializer, UserCriateSerializer
from utils import generate_random_string, generate_random_digits
from users.validators import validate_phone_number


@method_decorator(csrf_exempt, name='dispatch')
class UserGetCreat(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserCriateSerializer

    def post(self, request):
        data = request.data

        phone = data.get('phone')
        validate_phone_number(phone)
        user, _ = get_user_model().objects.get_or_create(phone=phone)
        user.auth_number = generate_random_digits()
        user.save()
        time.sleep(2)
        print(user.auth_number)

        response = redirect('users_api:auth', user.id)
        return response


class UserLogin(generics.UpdateAPIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    queryset = get_user_model().objects.all()
    serializer_class = UserSICSerializer

    def get(self, request, *args, **kwargs):
        return Response(data={'messenger': 'Введите код авторизации'},
                        status=HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if not user.invite_code:
            user.invite_code = generate_random_string()
            user.save()

        data = request.data
        auth_number = data.get('auth_number')
        if user.auth_number != auth_number:
            return Response(status=HTTP_400_BAD_REQUEST)
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key}, status=HTTP_202_ACCEPTED)


class UserGetUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, UserAndRoleVerification]
    serializer_class = UserSICSerializer
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UserSICSerializer
        return UserDetailSerializer

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        stranger_invite_code = request.data.get('stranger_invite_code')
        if not user.stranger_invite_code:
            users = get_user_model().objects.filter(invite_code=stranger_invite_code)
            if users:
                serializer = self.get_serializer(user, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=HTTP_202_ACCEPTED)
            return Response(data={'messenger': 'Не верный код'})
        return Response(data={'messenger': 'Вы уже активировали инвайт код'}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        invite_user = get_user_model().objects.filter(stranger_invite_code=user.invite_code)
        user.invite_user = invite_user
        serializer = self.get_serializer(user)
        data = serializer.data
        return Response(data, status=HTTP_200_OK)
