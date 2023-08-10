from django.urls import path, reverse
from .views import LoginUserView, RegisterUserView, CreateLandlordProfileView, CreateProfileView, LogoutUserView, ActivateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('finish_landlord_profile', login_required(CreateLandlordProfileView.as_view(), login_url='register'), name='finish_landlord_profile'),
    path('finish_profile', login_required(CreateProfileView.as_view(), login_url='login'), name='finish_profile'),
    path('logout', login_required(LogoutUserView.as_view()), name='logout'),
    path('activate/<str:uidb64>/<str:token>/', login_required(ActivateView.as_view()), name='activate'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')
]