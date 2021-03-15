from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from login.models import Login, Registration
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class RegisterView(generic.CreateView):
	model = Registration
	form_class = UserCreationForm
	template_name = 'login/registration.html'
	success_url = reverse_lazy('service:home')


class LoginView(generic.CreateView):
	model = Login
	template_name = 'login/user_login.html'
