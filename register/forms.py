from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerform(UserCreationForm):
    email = forms.EmailField()
    registration_no = forms.CharField()

    class Meta:
        model= User
        fields = ['username', 'email', 'registration_no', 'password1', 'password2']