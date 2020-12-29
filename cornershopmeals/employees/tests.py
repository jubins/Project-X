from django.test import TestCase
from django.contrib.auth.models import User


class Employee(TestCase):

    def test_retrieving_food_admin(self):
        employee = User.objects.filter(is_staff=True)
        employee = employee[0] if employee else None
        self.assertEqual(employee.is_staff, True)

    def test_retrieving_employee(self):
        employee = User.objects.filter(is_staff=False)
        employee = employee[0] if employee else None
        self.assertEqual(employee.is_staff, True)
