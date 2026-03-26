from django import forms
from django.contrib.auth.models import User

from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('user_site', 'user_pic')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('user_site', 'user_pic')

