from django.shortcuts import render
from django.views import generic
from login.models import Login
from django.urls import reverse_lazy

# Create your views here.


class ProfileView(generic.CreateView):
    template_name = 'userprofile/user_profile.html'
    model = Login
    success_url = reverse_lazy('userprofile:user_home')
    fields = ("name", "password")