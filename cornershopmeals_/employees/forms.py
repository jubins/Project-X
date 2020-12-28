from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from . models import Employee


class EmployeeRegisterForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'is_admin']
