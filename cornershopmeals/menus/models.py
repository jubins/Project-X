from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
        editable=True,
        help_text='Menu available date.',
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
    menu_option_6 = models.CharField(
        max_length=300,
        help_text='Option 6 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_7 = models.CharField(
        max_length=300,
        help_text='Option 7 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_8 = models.CharField(
        max_length=300,
        help_text='Option 8 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_9 = models.CharField(
        max_length=300,
        help_text='Option 9 in the menu',
        null=True,
        blank=True,
        editable=True,
    )
    menu_option_10 = models.CharField(
        max_length=300,
        help_text='Option 10 in the menu',
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


class MenuEmployee(models.Model):
    menu_id = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )
    employee_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        help_text='Date time when selection was modified.'
    )
    option_selected = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text='Option selected by the employee.'
    )
    customization_notes = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text='Customization notes',
    )

    def __str__(self):
        return self.customization_notes

    class Meta:
        db_table = 'menu_employees'
