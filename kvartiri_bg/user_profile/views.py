from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, FormView, TemplateView
from django.contrib.auth.views import PasswordChangeView
from auth_views.models import *
from properties.forms import ReactionForm
from django.http import HttpResponse, HttpResponseRedirect
from properties.models import Property
from django.urls import reverse_lazy
from django.shortcuts import redirect
from auth_views.forms import CreateLandlordProfileForm, CreateProfileForm
from mixins import UserContextMixin, SuccessMixin
from properties.models import Property
from properties.models import MessageFromLandlord, MessageFromTenant, Favourite
import re
from itertools import chain
from mixins import GetContextBasedOnType




def create_profile_update_view(model_class, form_klass):
    class UpdateViewClass(UserContextMixin, SuccessMixin, UpdateView):
        model = model_class
        form_class = form_klass
        template_name = 'profile_templates/edit_profile.html'
    
    return UpdateViewClass

def create_delete_profile_view(model_class):
    class DeleteProfile(DeleteView):
        model = model_class
        success_url = reverse_lazy('login')
        template_name = 'profile_templates/confirm_delete.html'


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

def create_profile_view(model_class, context_object):
    class ProfileView(UserContextMixin, DetailView):
        model = model_class
        context_object_name = context_object
        template_name = 'profile_templates/profile_page.html'

    return ProfileView


 
class MessagesView(GetContextBasedOnType, ListView):
    """
    User's messages - sent and received
    """
    template_name = 'profile_templates/my_messages.html'
    context_object_name = 'messages'
    paginate_by = 6
    

    def get_queryset(self) -> QuerySet[Any]:

        if self.request.user.type == 'TENANT':
            sent = MessageFromLandlord.objects.filter(recipient_id=Profile.objects.get(user_id=self.request.user.id).pk)
            received = MessageFromTenant.objects.filter(sender_id=Profile.objects.get(user_id=self.request.user.id).pk)
        else:
            sent = MessageFromLandlord.objects.filter(sender_id=LandlordProfile.objects.get(user_id=self.request.user.id).pk)
            received = MessageFromTenant.objects.filter(recipient_id=LandlordProfile.objects.get(user_id=self.request.user.id).pk)

   
        all_messages = list(chain(sent, received))
        return all_messages[::-1]

class ReplyMessage(FormView):
    """
    Handles replies to messages
    """
    template_name = 'profile_templates/reply.html'
    form_class = ReactionForm
    context_object_name = 'messages'
    success_url = reverse_lazy('messages')


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        regex = re.compile('\d+$')
        message_id = regex.search(self.request.path).group(0)

        sender = None
        recipient = None
        
        if self.request.user.type == 'LANDLORD':
            message = MessageFromTenant.objects.get(pk=message_id)
            sender  = User.objects.get(pk=Profile.objects.get(pk=message.sender_id).user_id).email
            recipient = User.objects.get(pk=LandlordProfile.objects.get(pk=message.recipient_id).user_id).email

        else:
            message =  MessageFromLandlord.objects.get(pk=message_id)  
            sender  = User.objects.get(pk=LandlordProfile.objects.get(pk=message.sender_id).user_id).email
            recipient = User.objects.get(pk=Profile.objects.get(pk=message.recipient_id).user_id).email 

        sender, recipient = recipient, sender
        context['sender'] = sender
        context['recipient'] = recipient

        return context 

    def form_valid(self, form):
        regex = re.compile('\d+$')
        message_id = regex.search(self.request.path).group(0)
        
        if self.request.user.type == 'LANDLORD':
            message =  MessageFromTenant.objects.get(pk=message_id)
            sender = LandlordProfile.objects.get(pk=message.recipient_id)
            recipient  = Profile.objects.get(pk=message.sender_id)

        else:
            message = MessageFromLandlord.objects.get(pk=message_id)
            sender = Profile.objects.get(pk=message.recipient_id)
            recipient  = LandlordProfile.objects.get(pk=message.sender_id)
            
            

        property = Property.objects.get(pk=message.property_id)
        msg_content = form.cleaned_data['msg_content']


        if self.request.user.type == 'LANDLORD':
            new_message = MessageFromLandlord(
                sender = sender,
                recipient=recipient,
                msg_content = msg_content,
                property = property
            )

        else:
            new_message = MessageFromTenant(
                sender = sender,
                recipient = recipient,
                msg_content = msg_content,
                property = property
            )


        new_message.save()
        return super().form_valid(form)

    def form_invalid(self, form: Any) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)


class ChangePasswordView(SuccessMixin, PasswordChangeView):
    """
    Handles password change.
    """
    template_name = 'auth_templates/change_password.html'


class FavouritesView(GetContextBasedOnType, ListView):
    """
    View that displays tenant's favourite properties
    """
    model = Favourite
    template_name = 'profile_templates/favourite_properties.html'
    context_object_name = 'favourites'
    paginate_by = 9

    def get_queryset(self):
        profile = Profile.objects.get(user_id=self.request.user.id)

        try:
            favourite = Favourite.objects.all().filter(profile=profile)[0]
            favourite = favourite.property.all()
        except self.model.DoesNotExist:
            favourite = QuerySet(None)
    
        return favourite

class LandlordOfferings(ListView):
    """
    Landlord's offerings
    """
    model = Property
    paginate_by = 10
    template_name = 'profile_templates/landlord_properties.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return self.model.objects.filter(landlord_id = LandlordProfile.objects.get(user_id=self.request.user.id).pk)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['landlord'] = LandlordProfile.objects.get(user_id=self.request.user.id)
        return context
    

EditTenantProfile = create_profile_update_view(Profile, CreateProfileForm) 
EditLandlordProfile = create_profile_update_view(LandlordProfile, CreateLandlordProfileForm)
DeleteTenantProfile = create_delete_profile_view(Profile)
DeleteLandlordProfile = create_delete_profile_view(LandlordProfile)
LandlordProfileView = create_profile_view(LandlordProfile, 'landlord')
ProfileView = create_profile_view(Profile, 'profile')

