from django.urls import path
from .views import LoginUserView, RegisterUserView, CreateProfileView

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('finish_profile', CreateProfileView.as_view(), name='finish_profile')
]