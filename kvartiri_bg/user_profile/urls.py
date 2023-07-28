from django.urls import path
from .views import ProfileView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('profile/<int:pk>', login_required(ProfileView.as_view()), name='profile')
]
