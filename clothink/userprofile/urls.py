from django.urls import path
from userprofile import views
from django.conf import settings
from django.conf.urls.static import static
from userprofile.views import success, user_image_view

app_name = 'userprofile'

urlpatterns = [
	path('userprofile/', views.ProfileView.as_view(), name='user_home'),
	path('profile_auth/', views.profile_auth, name='profile_auth'),
	path('image_upload/', user_image_view, name='image_upload'),
	path('success/', success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
