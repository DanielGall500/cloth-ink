from django.shortcuts import render
from django.views import generic
from login.models import Login, Registration
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class RegisterView(generic.ListView):
	model = Registration
	form_class = UserCreationForm
	#context = {'form': form}
	template_name = 'login/registration.html'


class LoginView(generic.ListView):
	model = Login
	template_name = 'login/user_login.html'
