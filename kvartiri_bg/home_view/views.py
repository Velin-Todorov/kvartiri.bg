from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from auth_views.models import LandlordProfile, Profile
from properties.models import Property
from mixins import GetContextBasedOnType

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home_templates/home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        last_5_properties = Property.objects.all().order_by('-created_at')[:5]
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['properties'] = last_5_properties

        if self.request.user.is_authenticated:
            if self.request.user.type == 'LANDLORD':
                context['landlord'] = LandlordProfile.objects.get(user_id=self.request.user.pk)
            else:
                print(self.request.user.pk)
                context['profile'] = Profile.objects.get(user_id=self.request.user.pk)

        return context



class ChooseYourProfile(TemplateView):
    template_name = 'pre_register.html'
        
    
class DisplayProperties(GetContextBasedOnType, ListView):
    model = Property
    paginate_by = 10
    template_name = 'property_templates/all_properties.html'
    context_object_name = 'properties'

    def get_queryset(self) -> QuerySet[Any]:
        qs = Property.objects.all()
        query_param = self.request.GET.get('city')

        if query_param is not None:
            qs = qs.filter(town=query_param.upper())
        
        return qs


class RentOutPlace(GetContextBasedOnType, TemplateView):
    template_name = 'rent_out.html'


class AboutPage(GetContextBasedOnType, TemplateView):
    template_name = 'home_templates/about.html'

class HowToUseIt(GetContextBasedOnType, TemplateView):
    template_name='home_templates/how_to_use.html'
