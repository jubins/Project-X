from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Employee(AbstractUser):
    employee_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text='Employee id.',
    )
    username = models.CharField(
        help_text='Employee username.',
        null=True,
        max_length=100,
    )
    first_name = models.CharField(
        editable=True,
        help_text='First name of the employee.',
        null=False,
        max_length=100,
    )
    last_name = models.CharField(
        editable=True,
        help_text='Last name of the employee.',
        null=False,
        max_length=100,
    )
    email = models.EmailField(
        editable=True,
        help_text='Email of the employee.',
        unique=True,
        null=False,
    )
    is_admin = models.BooleanField(
        editable=True,
        default=False,
        null=False,
        help_text='If the employee is admin.',
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        null=False,
        help_text='Date when the employee was modified.'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

    class Meta:
        db_table = 'employees'

