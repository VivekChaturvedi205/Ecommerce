"""Pluskart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from main import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('Reg/', views.Reg, name="Reg"),
    path('Reg_process/', views.Reg_Process, name="Reg_proc"),
    path('login_process/', views.login_Process, name="login_proc"),
    path('logout/', views.logout, name="logout"),
    path('change/', views.change, name="change"),
    path('change_procc/', views.change_password, name="change_procss"),
    path('search', views.search, name="search"),
]
