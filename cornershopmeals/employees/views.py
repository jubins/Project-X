from django.shortcuts import render, redirect
from employees.forms import EmployeeRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from employees.models import Employee


def Register(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # employee = Employee()
            # employee.first_name = request.POST.get('first_name')
            # employee.last_name = request.POST.get('last_name')
            # employee.email = request.POST.get('email')
            # employee.password = request.POST.get('password1')
            # employee.is_admin = request.POST.get('is_admin', False)
            # print('JJpass: ', request.POST)
            # employee.save()
            return redirect("/profile")
    else:
        form = EmployeeRegisterForm()
    context = {'form': form}
    return render(request, 'employees/register.html', context)


