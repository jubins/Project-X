from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import CreateNewMenu
from . models import Menu, MenuEmployee
from . import slack
from configparser import ConfigParser

env = ConfigParser()
env.read('env.ini')


def create_menu(request):
    if request.method == 'POST':
        menu = CreateNewMenu(request.POST)
        if menu.is_valid():
            menu.save()
        m = Menu.objects.latest('menu_date')
        return show_latest_menu(request=request, menu=m)
    else:
        menu = CreateNewMenu()
    content = {'form': menu}
    return render(request, 'menus/create_menus.html', content)


def view_selections(request, menu_id, employee_id):
    if request.method == 'GET' and request.GET.get('slack'):
        slack_notify(request)

    if request.method == 'GET':
        menu = Menu.objects.filter(menu_id=menu_id)
        menu = menu[0] if menu else None
        employees = User.objects.all()
        selections = list()
        for e in employees:
            s = dict()
            s['employee_username'] = e.username
            s['employee_name'] = e.first_name + ' ' + e.last_name
            me = MenuEmployee.objects.filter(menu_id=menu_id, employee_id_id=e.id)
            s['employee_selection_id'] = me[0].option_selected if me else None
            s['employee_customization_notes'] = me[0].customization_notes if me else None
            s['employee_last_modified_at'] = me[0].modified_at if me else None
            s['employee_selection_description'] = getattr(menu, str(s['employee_selection_id']), None)
            selections.append(s)
        content = {'selections': selections, 'menu': menu}
        return render(request, 'menus/view_selections.html', content)
    return render(request, 'menus/view_selections.html', {'selections': None})


def make_selection(request, menu_id, employee_id):
    if request.method == 'GET':
        menu = Menu.objects.filter(menu_id=menu_id)
        menu = menu[0] if menu else None
        me = MenuEmployee.objects.filter(menu_id=menu_id, employee_id=employee_id)
        me = me[0] if me else None
        option_selected = me.option_selected.split('_')[-1] if me else None
        content = {'menu': menu, 'menu_employee': me, 'employee_id': employee_id, 'option': option_selected}
        return render(request, 'menus/choose_option.html', content)
    elif request.method == 'POST':
        form = request.POST
        option_selected = form.get('option').split(f'{menu_id}_{employee_id}_option')[-1]
        try:
            menu = Menu.objects.filter(menu_id=menu_id)
            menu = menu[0] if menu else None
            me = MenuEmployee.objects.filter(menu_id=menu_id, employee_id=employee_id)
            me = me[0] if me else None
            if me:
                me.option_selected = f'menu_option_{option_selected}'
                me.customization_notes = form.get(f'{menu_id}_{employee_id}_notes')
                me.save()
            else:
                me = MenuEmployee()
                me.menu_id_id = menu_id
                me.employee_id_id = employee_id
                me.option_selected = f'menu_option_{option_selected}'
                me.customization_notes = form.get(f'{menu_id}_{employee_id}_notes')
                me.save()
            content = {'menu': menu, 'menu_employee': me, 'employee_id': employee_id, 'option': option_selected}
            messages.success(request, 'Menu option submitted.')
            return render(request, 'menus/choose_option.html', content)
        except Exception as err:
            messages.error(request, str(err))
            return render(request, 'menus/choose_option.html', {'menu': None, 'menu_employee': None, 'employee_id': None, 'option': None})


def show_all_menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus/all_menus.html', context={'menus': menus})


def show_latest_menu(request, menu=None, menu_id=None):
    if request.method == 'GET' and request.GET.get('slack'):
        slack_notify(request)
    try:
        if not menu or not menu_id:
            menu = Menu.objects.latest('menu_date')
        return render(request, 'menus/menu.html', context={'menu': menu})
    except Menu.DoesNotExist:
        return HttpResponse("<h2> Sorry! There are no menus to show.</h3>")


def show_menu_by_id(request, menu_id=None):
    if request.method == 'GET' and request.GET.get('slack'):
        slack_notify(request)
    try:
        context = {'menu': None}
        if menu_id:
            menu = Menu.objects.filter(menu_id=menu_id)
            menu = menu[0] if menu else None
            context['menu'] = menu
        return render(request, 'menus/menu.html', context=context)
    except Menu.DoesNotExist:
        return HttpResponse("<h2> Sorry! There are no menus to show.</h3>")


def make_slack_menu_message(menu):
    menu_items = dict()
    menu_url = env['host'].get('heroku', 'https://cornershop-meals-app.herokuapp.com/') + 'menu/' + str(menu.menu_id) + '/'
    menu_items['Menu Url'] = menu_url
    menu_items['Option 1'] = menu.menu_option_1
    if menu.menu_option_2:
        menu_items['Option 2'] = menu.menu_option_2
    if menu.menu_option_3:
        menu_items['Option 3'] = menu.menu_option_3
    if menu.menu_option_4:
        menu_items['Option 4'] = menu.menu_option_4
    if menu.menu_option_5:
        menu_items['Option 5'] = menu.menu_option_5
    if menu.menu_option_6:
        menu_items['Option 6'] = menu.menu_option_6
    if menu.menu_option_7:
        menu_items['Option 7'] = menu.menu_option_7
    if menu.menu_option_8:
        menu_items['Option 8'] = menu.menu_option_8
    if menu.menu_option_9:
        menu_items['Option 9'] = menu.menu_option_9
    if menu.menu_option_10:
        menu_items['Option 10'] = menu.menu_option_10

    message_str = "Hello!\nI'm sharing with you today's menu :) \n"
    for k, v in menu_items.items():
        message_str += f'{k}: {v}\n'
    message_str += "Go to the menu url before 11 am CLT to make your selection.\nHave a nice day!\nBest,\nNora"
    return message_str


def slack_notify(request):
    try:
        ids = request.GET.get('slack').split('_')
        menu_id, employee_id = ids[1], ids[2]
        menu = Menu.objects.filter(menu_id=str(menu_id))
        menu = menu[0] if menu else None
        menu_message = make_slack_menu_message(menu)
        response = slack.send_slack_message(menu_message)
        if response.status_code == 200:
            messages.success(request, 'Slack reminders sent.')
        else:
            err = response.text
            messages.error(request, 'Slack error: '+err)
    except Exception as err:
        messages.error(request, 'Slack error: '+str(err))

