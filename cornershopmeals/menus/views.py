from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import CreateNewMenu
from . models import Menu, MenuEmployee


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
    if request.method == 'GET':
        menu = Menu.objects.filter(menu_id=menu_id)
        menu = menu[0] if menu else None
        employees = User.objects.all()
        selections = list()
        for e in employees:
            s = dict()
            s['employee_username'] = e.username
            s['employee_name'] = e.first_name + ' ' + e.last_name
            me = MenuEmployee.objects.filter(menu_id=menu_id)
            s['employee_selection'] = me[0].option_selected if me else None
            s['employee_customization_notes'] = me[0].customization_notes if me else None
            s['employee_last_modified_at'] = me[0].modified_at if me else None
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
    try:
        if not menu or not menu_id:
            menu = Menu.objects.latest('menu_date')
        return render(request, 'menus/menu.html', context={'menu': menu})
    except Menu.DoesNotExist:
        return HttpResponse("<h2> Sorry! There are no menus to show.</h3>")


def show_menu_by_id(request, menu_id=None):
    try:
        context = {'menu': None}
        if menu_id:
            menu = Menu.objects.filter(menu_id=menu_id)
            menu = menu[0] if menu else None
            context['menu'] = menu
        return render(request, 'menus/menu.html', context=context)
    except Menu.DoesNotExist:
        return HttpResponse("<h2> Sorry! There are no menus to show.</h3>")


