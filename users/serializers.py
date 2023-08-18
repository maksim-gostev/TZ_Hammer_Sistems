from rest_framework import serializers

from users.models import User

class UserCriateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone',)


class UserSICSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'phone', 'auth_number', 'invite_code')
        fields = ('id', 'phone', 'invite_code', 'stranger_invite_code')



class UserDetailSerializer(serializers.ModelSerializer):
    invite_user = UserCriateSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'invite_code', 'phone', 'invite_user')
