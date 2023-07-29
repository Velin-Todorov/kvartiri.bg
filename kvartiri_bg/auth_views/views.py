from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .forms import RegistrationForm, LoginUserForm, CreateProfileForm, CreateLandlordProfileForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import views as auth_views, login, get_user_model, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Profile, User, LandlordProfile
# Create your views here

User = get_user_model()

class RegisterUserView(FormView):
    """
    Registers a User
    """
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('choose_profile')
    
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

        login(self.request, user)
        if type == 'LANDLORD':
            return redirect('finish_landlord_profile')

        elif type == 'TENANT':
            return redirect('finish_profile') 


    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginUserView(FormView):
    template_name = 'login.html'
    form_class = LoginUserForm
    

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        user = authenticate(self.request, email=email, password =password)
        
        if user is not None:
            login(self.request, user)
            if user.profile_finished:
                return redirect(reverse('profile', kwargs={'pk': user.pk}))
            else:
                if user.type == 'TENANT':
                    return redirect('finish_profile')
                elif user.type == 'LANDLORD':
                    return redirect('finish_landlord_profile')
        
        return super().form_valid(form)


    def form_invalid(self, form) -> HttpResponse:
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        print(self.request.user)
        return reverse('profile', kwargs={'pk':self.request.user.pk})



class LogoutUserView(auth_views.LogoutView):
    pass


class CreateProfileView(FormView, PermissionRequiredMixin):
    """
    Creates a tenant profile
    """
    form_class = CreateProfileForm
    template_name = 'create_profile.html'

    def form_valid(self, form):
        user = User.objects.filter(type='TENANT').last()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        looking_for = form.cleaned_data['looking_for']
        about = form.cleaned_data['about']
        budget = form.cleaned_data['budget']
        profile_picture = form.cleaned_data['profile_picture']

        Profile.objects.create(
            first_name = first_name,
            last_name = last_name,
            looking_for=looking_for,
            about=about,
            budget=budget,
            profile_finished = True,
            profile_picture=profile_picture,
            user_id = user.pk
        )

        user.profile_finished = True
        user.save()
        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)


    def get_success_url(self) -> str:
        user = Profile.objects.get(user_id = self.request.user.pk).pk
        return reverse('profile', kwargs={'pk':user})


class ChooseProfileView(TemplateView):
    template_name = 'choose_profile_type.html'


class CreateLandlordProfileView(FormView, PermissionRequiredMixin):
    form_class = CreateLandlordProfileForm
    template_name = 'create_landlord_profile.html'

    def form_valid(self, form):
        user = User.objects.filter(type='LANDLORD').last()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        about = form.cleaned_data['about']
        type = form.cleaned_data['type']
        profile_picture = form.cleaned_data['profile_picture']

        LandlordProfile.objects.create(
            first_name = first_name,
            last_name = last_name,
            about=about,
            profile_picture=profile_picture,
            profile_finished = True,
            type = type,
            user_id = user.last().pk
        )
        user.profile_finished = True
        user.save()
        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        user = LandlordProfile.objects.get(user_id = self.request.user.pk).pk
        return reverse('landlord_profile', kwargs={'pk':user})