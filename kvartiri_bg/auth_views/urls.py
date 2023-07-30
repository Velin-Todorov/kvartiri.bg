from django.urls import path, reverse
from .views import LoginUserView, RegisterUserView, CreateProfileView, ChooseProfileView, CreateLandlordProfileView, LogoutUserView, ActivateView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('choose_profile', login_required(ChooseProfileView.as_view(), login_url='register'), name='choose_profile'),
    path('finish_landlord_profile', login_required(CreateLandlordProfileView.as_view(), login_url='register'), name='finish_landlord_profile'),
    path('finish_profile', login_required(CreateProfileView.as_view(), login_url='login'), name='finish_profile'),
    path('logout', login_required(LogoutUserView.as_view()), name='logout'),
    path('activate/<str:uidb64>/<str:token>/', login_required(ActivateView.as_view()), name='activate')
]