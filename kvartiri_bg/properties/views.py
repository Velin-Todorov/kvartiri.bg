from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ChangePictures, ReactionForm
from django.views.generic import DetailView, UpdateView, DeleteView, FormView
from .models import Property, Picture, MessageFromTenant, Favourite
from .forms import CreateProperty
from django.urls import reverse
import re
from django.urls import reverse_lazy
from auth_views.models import LandlordProfile, Profile, User
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, User, Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
from mixins import LandlordOnlyMixin, TenantOnlyMixin
# Create your views here.

class CreateProperty(LandlordOnlyMixin, FormView):
    """
    Handles new property creation
    """
    model = Property
    permission_required = 'properties.add_property'
    form_class = CreateProperty
    template_name = 'property_templates/create_property.html'

    def form_valid(self, form):

        type = form.cleaned_data['type']
        price_per_month = form.cleaned_data['price_per_month']
        size = form.cleaned_data['size']
        town = form.cleaned_data['town']
        about = form.cleaned_data['about']
        address = form.cleaned_data['address']
        furnished = form.cleaned_data['furnished']
        utilities = form.cleaned_data['utilities_included']
    
        landlord = LandlordProfile.objects.get(user_id=self.request.user.id)
        images = self.request.FILES


        property = Property(
            type = type,
            price_per_month = price_per_month,
            size = size,
            town = town,
            about=about,
            address = address,
            furnished = furnished,
            utilities_included = utilities,
            landlord = landlord
        )
        property.save()

        for img in images.getlist('images'):
            picture = Picture(picture=img, property=property)
            picture.save()

        property.images = Picture.objects.filter(property_id=property.pk).first().picture
        property.save()
        return super().form_valid(form)
        
    def form_invalid(self, form) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        user = LandlordProfile.objects.get(user_id = self.request.user.pk).pk
        return reverse('landlord_offerings', kwargs={'pk':user})


class EditProperty(LandlordOnlyMixin, UpdateView):
    """
    Handles existing property editing
    """

    model = Property
    fields = [
        'type',
        'price_per_month',
        'size',
        'town',
        'address',
        'about',
        'images',
        'furnished',
        'utilities_included'
    ]
    template_name = 'property_templates/edit_property.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['picture_form'] = ChangePictures
        return context

    def get_success_url(self) -> str:
        user = LandlordProfile.objects.get(user_id = self.request.user.pk).pk
        return reverse('landlord_offerings', kwargs={'pk':user})

class DeleteProperty(LandlordOnlyMixin, DeleteView):
    """
    Handles property deletion
    """

    model = Property
    template_name = 'confirm_delete.html'

    def get_success_url(self) -> str:
        user = LandlordProfile.objects.get(user_id = self.request.user.pk).pk
        return reverse('landlord_offerings', kwargs={'pk':user})

    

class PropertyView(DetailView):
    model = Property
    template_name = 'property_templates/property_details.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        created = self.get_object().created_at
        
        if self.request.user.is_authenticated:
            if self.request.user.type == 'TENANT':
                profile = Profile.objects.get(user_id=self.request.user.pk)
                context['profile'] = profile
                favourites = Favourite.objects.all()

                if favourites:
                    try:
                        favourites = favourites.get(profile=profile)
                        context['favourites'] = favourites.property.all()
                    except:
                        context['favourites'] = []

        landlord = LandlordProfile.objects.get(pk=self.get_object().landlord_id)
        pictures = Picture.objects.filter(property_id=self.get_object().pk)
        user = self.request.user
        context['landlord'] = landlord
        context['user'] = user
        context['created'] = created
        context['pictures'] = pictures
        return context


class ReactToProperty(TenantOnlyMixin, FormView):
    """
    Handles reactions on tenant side.
    """

    model= Property
    form_class = ReactionForm
    template_name = 'property_templates/react_to_property.html'
    fields = ['msg_content']
    success_url = reverse_lazy('messages')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        regex = re.compile('\d+$')
        property_id = regex.search(self.request.path).group(0)

        property= Property.objects.get(pk=property_id)
        landlord = LandlordProfile.objects.get(pk=property.landlord_id)
        recipient = User.objects.get(pk=landlord.user_id)
        
        context['sender'] = self.request.user.email
        context['recipient'] = recipient
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        regex = re.compile('\d+$')
        property_id = regex.search(self.request.path).group(0)

        property= Property.objects.get(pk=property_id)
        landlord = LandlordProfile.objects.get(pk=property.landlord_id)
        profile = Profile.objects.get(user_id = self.request.user.pk)
        msg_content = form.cleaned_data['msg_content']

        message = MessageFromTenant(
            sender=profile,
            recipient=landlord,
            msg_content = msg_content,
            property = property
        )

        message.save()

        return super().form_valid(form)
    
    def form_invalid(self, form: Any) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)


def favourite_add(request, pk):
    property = get_object_or_404(Property, id=pk)
    profile = Profile.objects.get(user_id=request.user.id)
    favourite, created = Favourite.objects.get_or_create(profile=profile)
    favourite.property.add(property)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def removed_favourite(request, pk):
    property = get_object_or_404(Property, id=pk)
    profile = Profile.objects.get(user_id=request.user.id)
    favourite = Favourite.objects.get(profile=profile)
    favourite.property.remove(property)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

