from typing import Any, Dict
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import PasswordChangeView
from auth_views.models import *
from .forms import *
from properties.models import Property
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from auth_views.forms import CreateLandlordProfileForm, CreateProfileForm
from .mixins import UserContextMixin, SuccessMixin
from properties.models import Property


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


        def form_valid(self, form):
            try:
                user = self.request.user

                if self.request.user.type == 'LANDLORD':
                    profile = LandlordProfile.objects.get(user_id=user.pk)
                
                else:
                    profile = Profile.objects.get(user_id=user.pk)
                    
                user.delete()
                profile.delete()
                
            except Exception as e:
                print(e)

            return redirect(self.success_url)

    return DeleteProfile

# Create your views here.
class ProfileView(UserContextMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile_page.html'



class LandlordProfileView(UserContextMixin, DetailView):
    model = LandlordProfile
    context_object_name = 'landlord'
    template_name = 'landlord_profile.html'
    


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


class ChangePasswordView(SuccessMixin, PasswordChangeView):
    """
    Handles password change.
    """
    template_name = 'change_password.html'


class FavouritesView(DetailView):
    """
    View that displays user's favourite properties
    """
    pass

class LandlordOfferings(ListView):
    """
    Landlord's offerings
    """
    model = Property
    paginate_by = 10
    template_name = 'landlord_properties.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return self.model.objects.filter(landlord_id = LandlordProfile.objects.get(user_id=self.request.user.id).pk)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['landlord'] = LandlordProfile.objects.get(user_id=self.request.user.id)
        return context
    

EditTenantProfile = create_profile_update_view(Profile, CreateProfileForm, 'edit_profile.html') 
EditLandlordProfile = create_profile_update_view(LandlordProfile, CreateLandlordProfileForm, 'edit_profile.html')
DeleteTenantProfile = create_delete_profile_view(Profile)
DeleteLandlordProfile = create_delete_profile_view(LandlordProfile)


