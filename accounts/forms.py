from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django import forms


class UserForm(UserCreationForm):
    name = forms.CharField(label="이름")
    nickname = forms.CharField(label="닉네임")
    user_type = forms.IntegerField(label="사용자타입")

    class Meta:
        model = User
        fields = ("username", "name", "nickname", "user_type")
