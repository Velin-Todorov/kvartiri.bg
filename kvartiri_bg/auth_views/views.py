from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import View
from .forms import RegistrationForm, LoginUserForm, CreateProfileForm, CreateLandlordProfileForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import views as auth_views, login, get_user_model, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Profile, User, LandlordProfile
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .tokens import account_activation_token
from .utils import *
from django.contrib.auth.models import Group
from mixins import TenantOnlyMixin, LandlordOnlyMixin
# Create your views here

landlord_group, created = Group.objects.get_or_create(name='Landlord')
tenant_group, created = Group.objects.get_or_create(name='Tenants')



landlord_group.save()
tenant_group.save()

User = get_user_model()


class RegisterUserView(FormView):
    """
    Registers a User
    """
    form_class = RegistrationForm
    template_name = 'auth_templates/registration.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        type = form.cleaned_data['type']
                
        user = User(
            email=email, 
            password=make_password(password),
            type=type 
        )
        user.save()
        activateEmail(self.request, user)

        login(self.request, user)
        if type == 'LANDLORD':
            user.groups.add(landlord_group)
            return redirect('finish_landlord_profile')

        elif type == 'TENANT':
            user.groups.add(tenant_group)
            return redirect('finish_profile') 


    def form_invalid(self, form):
        return super().form_invalid(form)
    

class LoginUserView(FormView):
    template_name = 'auth_templates/login.html'
    form_class = LoginUserForm
    

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            if user.profile_finished:
                if user.type == 'TENANT':
                    tenant = Profile.objects.get(user_id=user.pk)
                    return redirect(reverse('profile', kwargs={'pk': tenant.pk}))
                else:
                    landlord = LandlordProfile.objects.get(user_id = user.pk)
                    return redirect(reverse('landlord_profile', kwargs={'pk': landlord.pk}))

            else:
                if user.type == 'TENANT':
                    return redirect('finish_profile')
                elif user.type == 'LANDLORD':
                    return redirect('finish_landlord_profile')
        else:
            messages.error(self.request, 'Invalid Credentials!')
            return super().form_invalid(form)


    def form_invalid(self, form) -> HttpResponse:
        print(self.request.user.type)
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse('profile', kwargs={'pk':self.request.user.pk})



class LogoutUserView(auth_views.LogoutView):
    pass


class ActivateView(View):
    def get_user_from_email_verification_token(self, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            user = None

        #if user is not None and account_activation_token.check_token(user, token):
        if user is not None:
            return user
  
        return None

    
    def get(self, request, uidb64, token):
        print(token)
        user = self.get_user_from_email_verification_token(uidb64, token)
        print(user)
        user.email_confirmed = True
        user.save()
        messages.success(request, message='You have verified your email successfully!')
        if not user.profile_finished: 
            if user.type == 'TENANT':
                return redirect('finish_profile')
            else:
                return redirect('finish_landlord_profile')
        
        return redirect('login')



class CreateProfileView(TenantOnlyMixin, FormView):
    """
    Creates a tenant profile
    """
    form_class = CreateProfileForm
    template_name = 'profile_templates/create_profile.html'

    def form_valid(self, form):
        user = User.objects.filter(type='TENANT').last()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        looking_for = form.cleaned_data['looking_for']
        about = form.cleaned_data['about']
        budget = form.cleaned_data['budget']
        profile_picture = form.cleaned_data['profile_picture']
        phone_number = form.cleaned_data['phone_number']
        
        profile = Profile.objects.create(
            first_name = first_name,
            last_name = last_name,
            looking_for=looking_for,
            about=about,
            budget=budget,
            phone_number=phone_number,
            profile_finished = True,
            profile_picture=profile_picture,
            user_id = user.pk
        )

        profile.save()
        user.profile_finished = True
        user.save()
        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)


    def get_success_url(self) -> str:
        user = Profile.objects.get(user_id = self.request.user.pk).pk
        return reverse('profile', kwargs={'pk':user})


class CreateLandlordProfileView(LandlordOnlyMixin, FormView):
    form_class = CreateLandlordProfileForm
    template_name = 'profile_templates/create_profile.html'

    def form_valid(self, form):
        user = User.objects.filter(type='LANDLORD').last()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        location = form.cleaned_data['location']
        about = form.cleaned_data['about']
        type = form.cleaned_data['type']
        profile_picture = form.cleaned_data['profile_picture']
        phone_number = form.cleaned_data['phone_number']

        landlord = LandlordProfile.objects.create(
            first_name = first_name,
            last_name = last_name,
            about=about,
            type = type,
            phone_number = phone_number,
            profile_picture=profile_picture,
            location = location,
            profile_finished = True,
            user_id = user.pk
        )

        landlord.save()
        user.profile_finished = True
        user.save()
        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        user = LandlordProfile.objects.get(user_id = self.request.user.pk).pk
        return reverse('landlord_profile', kwargs={'pk':user})
    
