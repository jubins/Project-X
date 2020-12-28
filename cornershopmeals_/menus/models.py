from uuid import uuid4
from django.db import models
from employees.models import Employee
from django.utils import timezone

# Create your models here.


class Menu(models.Model):
    menu_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text='Menu id.',
    )
    menu_name = models.CharField(
        default="Today's menu",
        editable=True,
        help_text='Menu Name.',
        blank=False,
        null=False,
        max_length=100,
    )
    menu_date = models.DateTimeField(
        default=timezone.now,
        null=False,
        editable=False,
        help_text='Date the menu is available.',
    )
    menu_option_1 = models.CharField(
        max_length=300,
        help_text='Option 1 in the menu',
        null=True,
        editable=True,
    )
    menu_option_2 = models.CharField(
        max_length=300,
        help_text='Option 2 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_3 = models.CharField(
        max_length=300,
        help_text='Option 3 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_4 = models.CharField(
        max_length=300,
        help_text='Option 4 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_5 = models.CharField(
        max_length=300,
        help_text='Option 5 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    is_confirmed = models.BooleanField(
        help_text='Is menu confirmed.',
        default=True,
    )

    def __str__(self):
        return f'{self.menu_id}'

    class Meta:
        db_table = 'menus'

#
# class MenuCustomizations(models.Model):
#     menu_id = models.ForeignKey(
#         Menu,
#         on_delete=models.CASCADE,
#     )
#     employee_id = models.ForeignKey(
#         Employee,
#         on_delete=models.CASCADE,
#     )
#     customization_text = models.CharField(
#         max_length=500,
#         null=True,
#         help_text='Employee customizations',
#     )
#
#     def __str__(self):
#         return f'{self.menu_id}-{self.employee_id}-{self.customization_text}'
#
#     class Meta:
#         db_table = 'menu_customizations'
#

