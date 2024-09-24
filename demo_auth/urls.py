"""
URL configuration for demo_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from ui import views as ui_views
from cust import views as cust_views

urlpatterns = [
    path('', ui_views.login_page),
    path('login', cust_views.login_user),
    path('logout', cust_views.logout_user),
    path('signup', ui_views.signup_page),
    path('new/user', cust_views.add_user),
    path('reset/password', ui_views.reset_password_page),
    path('reset/pwd', cust_views.reset_password),
]
