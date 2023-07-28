from django.urls import path, reverse_lazy
from .views import ProfileView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('profile/<int:pk>', login_required(ProfileView.as_view(), login_url=reverse_lazy('login')), name='profile')
]
