from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('profile/<int:pk>', login_required(ProfileView.as_view(), login_url=reverse_lazy('login')), name='profile'),
    path('profile/<int:pk>/favourites', login_required(FavouritesView.as_view(), login_url=reverse_lazy('login')), name='profile_favourites'),
    path('profile/<int:pk>/edit_profile', login_required(EditTenantProfile.as_view(), login_url=reverse_lazy('login')), name='edit_profile'),

    path('landlord-profile/<int:pk>', login_required(LandlordProfileView.as_view(), login_url=reverse_lazy('login')), name='landlord_profile'),
    path('landlord-profile/<int:pk>/offerings', login_required(LandlordOfferings.as_view(), login_url=reverse_lazy('login')), name='landlord_offerings'),
    path('landlord-profile/<int:pk>/edit_profile', login_required(EditLandlordProfile.as_view(), login_url=reverse_lazy('login')), name='edit_landlord'),

    path('delete_tenant/<int:pk>', login_required(DeleteTenantProfile.as_view(), login_url='login'), name='delete_tenant'),
    path('delete_landlord/<int:pk>', login_required(DeleteLandlordProfile.as_view(), login_url='login'), name='delete_landlord'),
    path('change_password', login_required(ChangePasswordView.as_view(), login_url='login'), name='change_password'),

    path('messages', MessagesView.as_view(), name='messages'),
    path('reply/message/<int:pk>', ReplyMessage.as_view(), name="reply_message")
]
