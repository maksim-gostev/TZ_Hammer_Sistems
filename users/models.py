from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from users.validators import validate_phone_number


class User(AbstractUser):
    username = None
    email = None
    phone = models.CharField(unique=True, max_length=20, db_index=True)
    password = None
    auth_number = models.IntegerField(null=True, blank=True)
    invite_code = models.CharField(max_length=6, null=True, blank=True, db_index=True)
    stranger_invite_code = models.CharField(max_length=6, null=True, blank=True, db_index=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
