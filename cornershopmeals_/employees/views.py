from django.shortcuts import render, redirect
from . forms import EmployeeRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.backends import ModelBackend


def register(request):
    if request.method == 'POST':
        employee = EmployeeRegisterForm(request.POST)
        if employee.is_valid():
            employee.save()
            messages.success(request, 'Employee created successfully.')
            return redirect("/home")
    else:
        employee = EmployeeRegisterForm()
    context = {'form': employee}
    return render(request, 'employees/register.html', context)


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            print('JJform: ', form.cleaned_data, user)
            if user is not None:
                login(request, user)
                print('JJhere')
                messages.info(request, f"You are now logged in as {email}")
                return redirect('/home')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="employees/login.html",
                  context={"form": form})


def Logout(request):
    print('JJrequestLogout: ', request)
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
