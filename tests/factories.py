import factory
from django.contrib.auth import get_user_model
from pytest_factoryboy import register


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()