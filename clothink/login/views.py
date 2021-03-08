from django.shortcuts import render
from django.views import generic
from login.models import Login, Registration
# Create your views here.
class LoginView(generic.ListView):
	model = Login
	template_name = 'login/user_login.html'

class RegisterView(generic.ListView):
	model = Registration
	template_name = 'login/registration.html'