from django.test import TestCase

from . models import Menu, MenuEmployee
from . import slack

class MenusModelTests(TestCase):
    def test_retrieving_latest_menu(self):
        menu = Menu.objects.latest('menu_date')
        menu = menu[0] if menu else None
        self.assertEqual(menu.menu_option_1, 'Salad')

    def test_retrieving_menu_by_id(self):
        menu_id = 'df61c7fd-4d88-4aa6-9fa3-06633829cff9'
        menu = Menu.objects.filter(menu_id=menu_id)
        menu = menu[0] if menu else None
        self.assertEqual(menu.menu_option_1, 'Salad')

    def test_retrieving_menu_by_invalid_id(self):
        menu_id = 'af61c7fd-4d88-4aa6-9fa3-06633829cff9'
        menu = Menu.objects.filter(menu_id=menu_id)
        menu = menu[0] if menu else None
        self.assertEqual(menu, None)

    def test_slack_reminders(self):
        menu = """
        Hello!\n
        I'm sharing with you today's menu :)\n
        Menu Url: https://cornershop-meals-app.herokuapp.com/menu/6d8f7a44-dbdf-4c0d-8854-dcd2f11ae1c3/\n
        Option 1: Pizza\n
        Option 2: Pasta\n
        Option 3: Tiramisu\n
        Option 4: Cheese and Wine\n
        Go to the menu url before 11 am CLT to make your selection.\n
        Have a nice day!\n
        Best,\n
        Nora
        """
        response = slack.send_slack_message(menu)
        self.assertEqual(response.status_code, 200)


class MenusEmployeeModelTests(TestCase):

    def test_retrieving_selected_menu_option_for_a_menu_by_employee_id(self):
        menu_id = 'df61c7fd-4d88-4aa6-9fa3-06633829cff9'
        me = MenuEmployee.objects.filter(menu_id=menu_id, employee_id=1)
        me = me[0] if me else None
        self.assertEqual(me.option_selected, 'menu_option_4')

    def test_retrieving_menu_option_for_invalid_menu_id(self):
        menu_id = 'ds61c7fd-4d88-4aa6-9fa3-06633829cff9'
        me = MenuEmployee.objects.filter(menu_id=menu_id, employee_id=1)
        me = me[0] if me else None
        self.assertEqual(me, None)
