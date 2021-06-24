import os

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic
from userprofile.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import UserImageForm

# Create your views here.


class ProfileView(generic.CreateView):
    template_name = 'userprofile/user_profile.html'
    model = User
    success_url = reverse_lazy('service:home')
    fields = ("email", "profile_image",)


def profile_auth(request):

    if request.user.is_authenticated:
        return redirect('userprofile:user_home')
    else:
        return redirect('login:user_login')


def user_image_view(request):

    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():

            try:
                os.remove(request.user.profile_image.path)
            except:
                pass

            data = form.cleaned_data.get("profile_image")
            print(data)
            print(type(data))
            pic_name = request.user.email
            request.user.profile_image.save(pic_name, data)

            return redirect('userprofile:success')
    else:
        form = UserImageForm()

    return render(request, 'userprofile/profile_pic_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def view_pp(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        #all_users = User.objects.get(email=request.user)
        all_users = User.objects.all()
        return render(request, 'userprofile/profile_pic_view.html', {'profile_pics': all_users})
