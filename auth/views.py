from django.shortcuts import render
from auth import forms
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User

# Create your views here.

class Loginkar(LoginView):
    template_name = 'auth/login_vaccinecenter.html'
    redirect_authenticated_user = False

class Logoutkar(LogoutView):
    # template_name = 'vaccine_center/'
    # redirect_authenticated_user = True
    pass
