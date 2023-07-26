from django.urls import path
from .views import LoginUserView, RegisterUserView, CreateProfileView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('finish_profile', login_required(CreateProfileView.as_view(), login_url='login'), name='finish_profile')
]