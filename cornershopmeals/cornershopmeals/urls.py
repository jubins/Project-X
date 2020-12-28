"""cornershopmeals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import Index, About
from menus.views import create_menu, edit_menu, make_selection, show_latest_menu, show_all_menus
from employees.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('index/', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path("home/", show_all_menus, name="home"),
    path('menu/', show_latest_menu, name='todays_menu'),
    path('create_menu/', create_menu, name='create_menu'),
    path(r'edit_menu/<uuid:menu_id>/<int:employee_id>', edit_menu, name='edit_menu'),
    path(r'make_selection/<uuid:menu_id>/<int:employee_id>', make_selection, name='make_selection'),
    path('menu/<uuid:menu_id>/', show_latest_menu, name='menu'),
    path('signup/', signup, name='signup')

]
