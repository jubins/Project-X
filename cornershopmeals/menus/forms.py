from django.forms import ModelForm
from . models import Menu


class CreateNewMenu(ModelForm):
    class Meta:
        model = Menu
        fields = [
            'menu_name',
            'menu_date',
            'menu_option_1',
            'menu_option_2',
            'menu_option_3',
            'menu_option_4',
            'menu_option_5',
            'menu_option_6',
            'menu_option_7',
            'menu_option_8',
            'menu_option_9',
            'menu_option_10',
        ]
