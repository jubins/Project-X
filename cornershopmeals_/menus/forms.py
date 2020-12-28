from django import forms
from django.forms import ModelForm
from . models import Menu


class CreateNewMenu(ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_option_1',
                  'menu_option_2',
                  'menu_option_3',
                  'menu_option_4',
                  'menu_option_5',
                  ]
