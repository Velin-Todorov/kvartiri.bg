from typing import Any, Dict, Optional, Type
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from auth_views.models import *
from django import forms
from .forms import *
from django.urls import reverse, reverse_lazy
from auth_views.forms import CreateLandlordProfileForm, CreateProfileForm
from .mixins import UserContextMixin, SuccessMixin


def create_profile_update_view(model_class, form_klass, template):
    class UpdateViewClass(UserContextMixin, SuccessMixin, UpdateView):
        model = model_class
        form_class = form_klass
        template_name = template
    
    return UpdateViewClass

def create_delete_profile_view(model_class):
    class DeleteProfile(DeleteView):
        model = model_class
        success_url = reverse_lazy('login')
        template_name = 'confirm_delete.html'
    
    return DeleteProfile

# Create your views here.
class ProfileView(UserContextMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile_page.html'



class LandlordProfileView(DetailView):
    model = LandlordProfile
    context_object_name = 'landlord'
    template_name = 'landlord_profile.html'
    succes_url = reverse_lazy('home')


class MessagesView(DetailView):
    """
    User's messages - sent and received
    """
    pass


class LandlordMessages(DetailView):
    """
    Landlord Messages
    """
    pass



class FavouritesView(DetailView):
    """
    View that displays user's favourite properties
    """
    pass

class LandlordOfferings(DetailView):
    """
    Landlord's offerings
    """
    pass

class ChangePasswordView(SuccessMixin, PasswordChangeView):
    """
    Handles password change.
    """
    template_name = 'change_password.html'


EditTenantProfile = create_profile_update_view(Profile, CreateProfileForm, 'edit_profile.html')
EditLandlordProfile = create_profile_update_view(LandlordProfile, CreateLandlordProfileForm, 'edit_profile.html')
DeleteTenantProfile = create_delete_profile_view(Profile)
DeleteLandlordProfile = create_delete_profile_view(LandlordProfile)


