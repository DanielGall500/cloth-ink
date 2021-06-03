from django.urls import path
from login import views
from django.contrib.auth import logout

app_name = 'login'

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='user_login'),
	path('login_auth/', views.login_auth, name='login_auth'),
	path('logout/', views.logout_view, name='logout'),
	path('register/',views.RegisterView.as_view(), name='user_registration'),
]