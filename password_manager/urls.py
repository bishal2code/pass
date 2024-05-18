"""
URL configuration for password_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from userlog.views import *
from userdata.views import *



urlpatterns = [
    path('login',login_page),
    path('signup',signup_page),
    path('edit/<id>',edit_page),
    path('addnew',addnew),
    path('',index),
    path('logout',logout_page),
    path('delete/<id>',delete_id),
]
