from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from userprofile.models import User
from django.urls import reverse_lazy

# Create your views here.

#@login_required(login_url='service:home')
class ProfileView(generic.CreateView):
    template_name = 'userprofile/user_profile.html'
    model = User
    success_url = reverse_lazy('service:home')
    fields = ("name", "password")


def profile_auth(request):
    if(request.user.is_authenticated):
        return redirect('userprofile:user_home')
    else:
        return redirect('login:user_login')
