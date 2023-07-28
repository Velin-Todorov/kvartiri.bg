from django.shortcuts import render
from django.views.generic import DetailView
from auth_views.models import Profile


# Create your views here.
class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile_page.html'