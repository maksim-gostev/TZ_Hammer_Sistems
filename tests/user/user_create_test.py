import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_create_user(client):
    data = {
        'phone': '+79646869722'
    }

    response = client.post(reverse('users_api:user_create'), data=data)
    user = User.objects.filter(phone=data['phone']).first()

    assert response.status_code == 302
    assert user.phone == data['phone']
