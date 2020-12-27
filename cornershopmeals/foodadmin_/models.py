from uuid import uuid4

from django.db import models
from django.utils import timezone


# Create your models here.
class MenuItem(models.Model):
    menu_item_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text='Menu item id.',
    )
    name = models.CharField(
        null=False,
        max_length=100,
        help_text='Name of the menu item.',
    )
    description = models.TextField(
        help_text='Menu item description.',
        default=None,
        null=True,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu_items'


class Menu(models.Model):
    menu_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        null=False,
        help_text='Date when the menu is available.'
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return f"{self.created_at.strftime('%m/%d/%Y %H:%M')}"

    class Meta:
        db_table = 'menus'
