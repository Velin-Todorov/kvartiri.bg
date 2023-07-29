from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('profile/<int:pk>', login_required(ProfileView.as_view(), login_url=reverse_lazy('login')), name='profile'),
    path('profile/<int:pk>/messages', login_required(MessagesView.as_view(), login_url=reverse_lazy('login')), name='profile_messages'),
    path('profile/<int:pk>/favourites', login_required(FavouritesView.as_view(), login_url=reverse_lazy('login')), name='profile_favourites'),
    # path('profile/<int:pk>/edit_profile', login_required(EditProfile.as_view(), login_url=reverse_lazy('login')), name='edit_profile'),
]
