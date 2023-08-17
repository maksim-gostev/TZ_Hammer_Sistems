from rest_framework import serializers

from users.models import User


class UserUpdateIACodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'username', 'email', 'phone', 'password', 'user_invite', 'stranger_invite_code')
        fields = ('id', 'username', 'email', 'phone', 'password', 'auth_number', 'invite_code')

class UserSICSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'username', 'email', 'phone', 'password', 'auth_number', 'invite_code')
        fields = ('id', 'username', 'phone', 'invite_code', 'stranger_invite_code')


class InviteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone',)


class UserDetailSerializer(serializers.ModelSerializer):
    invite_user = InviteUserSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'invite_code', 'phone', 'invite_user')
