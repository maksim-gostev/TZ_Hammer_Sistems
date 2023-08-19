import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_get_user_authorization(client):
    user_create = {
        'phone': '+79646869754'
    }

    client.post(reverse('users_api:user_create'), data=user_create)

    user = User.objects.filter(phone=user_create['phone']).first()

    data = {
        'auth_number': user.auth_number
    }

    response_token = client.post(reverse('users_api:auth', kwargs={'pk': user.id}), data=data,
                                 content_type='application/json')

    token = response_token.json()['token']

    user = User.objects.filter(phone=user_create['phone']).first()

    expected = {
        "id": 1,
        "invite_code": user.invite_code,
        "phone": "+79646869754",
        "invite_user": []
    }

    response = client.get(reverse('users_api:user_get_update', kwargs={'pk': user.id}),
                          HTTP_AUTHORIZATION="Token " + token)

    assert response.status_code == 200
    assert response.json() == expected


@pytest.mark.django_db
def test_get_user_not_authorization(client):
    user_create = {
        'phone': '+79646869754'
    }

    expected = {
        "detail": "Authentication credentials were not provided."
    }

    client.post(reverse('users_api:user_create'), data=user_create)

    user = User.objects.filter(phone=user_create['phone']).first()

    response = client.get(reverse('users_api:user_get_update', kwargs={'pk': user.id}))

    assert response.status_code == 401
    assert response.json() == expected
