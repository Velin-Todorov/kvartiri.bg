from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from auth_views.models import LandlordProfile, Profile
from properties.models import Property

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        if self.request.user.is_authenticated:
            if self.request.user.profile_finished:
                if self.request.user.type == 'LANDLORD':
                    context['landlord_profile'] = LandlordProfile.objects.get(user_id=self.request.user.pk)
                else:
                    context['profile'] = Profile.objects.get(user_id=self.request.user.pk)

        return context


class ChooseYourProfile(TemplateView):
    template_name = 'pre_register.html'
        
    
class DisplayProperties(ListView):
    model = Property
    paginate_by = 10
    template_name = 'all_properties.html'
    context_object_name = 'properties'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            if self.request.user.type == 'LANDLORD':
                context['landlord_profile'] = LandlordProfile.objects.get(user_id=self.request.user.pk)
            else:
                context['profile'] = Profile.objects.get(user_id=self.request.user.pk)

        return context


class RentOutPlace(TemplateView):
    template_name = 'rent_out.html'

