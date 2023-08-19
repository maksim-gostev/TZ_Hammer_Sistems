import time

from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

from rest_framework.authtoken.models import Token
from frontend.forms import UserForm, UserInviteForm, UserSICForm
from utils import generate_random_digits, generate_random_string
from users.validators import validate_phone_number


def get_or_create_user(request):
    context = {
        'user_form': UserForm
    }
    if request.method == 'POST':
        phone = request.POST.get('phone')
        validate_phone_number(phone)
        user, _ = get_user_model().objects.get_or_create(phone=phone)
        user.auth_number = generate_random_digits()
        user.save()
        time.sleep(2)
        print(user.auth_number)
        response = redirect(f'auth/{user.id}')
        return response

    return render(request, 'frontend/index.html', context)


def userlogin(request, pk):
    context = {
        'form': UserInviteForm,
    }
    user = get_user_model().objects.get(pk=pk)

    if request.method == 'GET':
        context.update({'user': user})
        return render(request, 'frontend/login.html', context)

    if request.method == 'POST':

        auth_number = request.POST.get('auth_number')

        if not user.invite_code:
            user.invite_code = generate_random_string()
            user.save()

        if user.auth_number != int(auth_number):
            return render(request, 'frontend/error.html', {'messenger': 'Неверный код'})

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        response = redirect('frontend:user', user.id)
        return response

    return render(request, 'frontend/error.html', {'messenger': 'Не верный код'})


def userdetail(request, pk):
    context = {
        'form': UserSICForm
    }
    user = get_user_model().objects.get(pk=pk)

    if request.method == 'GET':

        invite_user = get_user_model().objects.filter(stranger_invite_code=user.invite_code)
        context.update({'user': user,
                        'invite_user': invite_user})
        return render(request, 'frontend/user_detail.html', context)

    elif request.method == 'POST':

        stranger_invite_code = request.POST.get('stranger_invite_code')

        if not user.stranger_invite_code:

            users = get_user_model().objects.filter(invite_code=stranger_invite_code)
            if users:
                user.stranger_invite_code = stranger_invite_code
                user.save()
                response = redirect('frontend:user', user.id)
                return response
            return render(request, 'frontend/error.html', {'messenger': 'Не верный код'})
        return render(request, 'frontend/error.html', {'messenger': 'Вы уже активировали инвайт код'})
