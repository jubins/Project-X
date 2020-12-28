from django.shortcuts import render, HttpResponse
from django.contrib import messages
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


def edit_menu(request, menu_id=None):
    menu = Menu.objects.filter(menu_id=menu_id)
    menu_employee = MenuEmployee.objects.filter(menu_id=menu_id)
    content = {'menu': menu, 'menu_employee': menu_employee}
    return render(request, 'menus/edit_menu.html', content)


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
            return render(request, 'menus/choose_option.html', {})


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

