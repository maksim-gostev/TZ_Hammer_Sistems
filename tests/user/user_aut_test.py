import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_login_user(client):
    user_create = {
        'phone': '+79646869754'
    }

    client.post(reverse('users_api:user_create'), data=user_create)

    user = User.objects.filter(phone=user_create['phone']).first()

    data = {
        'auth_number': user.auth_number
    }

    response = client.post(reverse('users_api:auth', kwargs={'pk': user.id}), data=data,
                           content_type='application/json')

    assert response.status_code == 202
