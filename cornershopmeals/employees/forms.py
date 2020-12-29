from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'password1', 'password2']

