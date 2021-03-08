from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='user_login'),
]