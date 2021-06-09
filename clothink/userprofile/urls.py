from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
	path('userprofile/', views.ProfileView.as_view(), name='user_home'),
]