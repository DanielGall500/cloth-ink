from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from login.models import Login, Registration
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, authenticate

class RegisterView(generic.CreateView):
	model = Registration
	form_class = UserCreationForm
	template_name = 'login/registration.html'
	success_url = reverse_lazy('service:home')


class LoginView(generic.CreateView):
	model = Login
	template_name = 'login/user_login.html'
	success_url = reverse_lazy('service:home')
	fields = ("name","password")

def login_auth(request):
    name = request.POST.get('name')
    password = request.POST.get('password')

    user = authenticate(request, username=name, password=password)

    if user is not None:
	    login(request, user)
	    return redirect('service:home')
    else:
        return redirect('login:user_registration')
