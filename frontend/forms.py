from django.forms import ModelForm

from users.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone']

class UserInviteForm(ModelForm):
    class Meta:
        model = User
        fields = ['auth_number']

class UserSICForm(ModelForm):
    class Meta:
        model = User
        fields = ['stranger_invite_code']