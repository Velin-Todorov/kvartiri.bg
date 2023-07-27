from django.urls import path
from .views import LoginUserView, RegisterUserView, CreateProfileView, ChooseProfileView, CreateLandlordProfileView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('choose_profile', login_required(ChooseProfileView.as_view(), login_url='register'), name='choose_profile'),
    path('finish_landlord_profile', login_required(CreateLandlordProfileView.as_view(), login_url='register'), name='finish_landlord_profile'),
    path('finish_profile', login_required(CreateProfileView.as_view(), login_url='login'), name='finish_profile')
]