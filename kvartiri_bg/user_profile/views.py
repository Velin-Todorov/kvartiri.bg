from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, TemplateView
from auth_views.models import Profile, LandlordProfile


# Create your views here.
class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile_page.html'


class MessagesView(DetailView):
    """
    User's messages - sent and received
    """
    pass

class FavouritesView(DetailView):
    """
    View that displays user's favourite properties
    """
    pass

class EditProfile(UpdateView):
    """
    View that handles profile updates
    """
    pass


class PasswordResestView:
    """
    Handles password reset
    """

class OffersView:
    """
    View that displays landlord's offerings
    """

