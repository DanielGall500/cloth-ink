from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, authenticate
from userprofile.models import User
from userprofile.admin import UserCreationForm, UserLoginForm


class RegisterView(generic.CreateView):
	model = User
	form_class = UserCreationForm
	template_name = 'login/registration.html'
	success_url = reverse_lazy('service:home')


class LoginView(generic.CreateView):
	model = User
	form_class = UserLoginForm
	template_name = 'login/user_login.html'
	success_url = reverse_lazy('service:home')


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("service:home")


def login_auth(request):
	if request.method == 'POST':
		email = request.POST.get('email','')
		password = request.POST.get('password','')
		
		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('service:home')
		else:
			return redirect('login:user_registration')
	else:
		return redirect('login:user_registration')
