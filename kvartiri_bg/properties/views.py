from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, FormView
from .models import Property, Picture
from .forms import CreateProperty
from django.urls import reverse
from django.forms import modelformset_factory
from auth_views.models import LandlordProfile, Profile

# Create your views here.

class CreateProperty(FormView):
    """
    Handles new property creation
    """
    model = Property
    form_class = CreateProperty
    template_name = 'create_property.html'

    def form_valid(self, form):

        type = form.cleaned_data['type']
        price_per_month = form.cleaned_data['price_per_month']
        size = form.cleaned_data['size']
        town = form.cleaned_data['town']
        address = form.cleaned_data['address']
        furnished = form.cleaned_data['furnished']
        utilities = form.cleaned_data['utilities_included']
    
        landlord = LandlordProfile.objects.get(user_id=self.request.user.id)
        images = self.request.FILES
        images_list = images.getlist('images')


        property = Property(
            type = type,
            price_per_month = price_per_month,
            size = size,
            town = town,
            images = images_list[0],
            address = address,
            furnished = furnished,
            utilities_included = utilities,
            landlord = landlord
        )
        property.save()
        for img in images.getlist('images'):
            picture = Picture(picture=img, property=property)
            picture.save()

        return super().form_valid(form)
        
    def form_invalid(self, form) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        user = LandlordProfile.objects.get(user_id = self.request.user.pk).pk
        return reverse('landlord_offerings', kwargs={'pk':user})


class EditProperty:
    """
    Handles existing property editing
    """
    pass

class DeleteProperty:
    """
    Handles property deletion
    """
    pass

class PropertyView(DetailView):
    model = Property
    template_name = 'property_details.html'


