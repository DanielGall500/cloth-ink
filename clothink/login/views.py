from django.shortcuts import render
from django.views import generic
from login.models import Login
# Create your views here.
class LoginView(generic.ListView):
	model = Login
	template_name = 'login/user_login.html'