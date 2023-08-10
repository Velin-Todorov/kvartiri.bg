from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from auth_views.models import LandlordProfile, Profile
from properties.models import Property
from mixins import GetContextBasedOnType

# Create your views here.
class IndexView(GetContextBasedOnType, TemplateView):
    template_name = 'home_templates/home.html'

class ChooseYourProfile(TemplateView):
    template_name = 'pre_register.html'
        
    
class DisplayProperties(GetContextBasedOnType, ListView):
    model = Property
    paginate_by = 10
    template_name = 'property_templates/all_properties.html'
    context_object_name = 'properties'

class RentOutPlace(TemplateView):
    template_name = 'rent_out.html'

