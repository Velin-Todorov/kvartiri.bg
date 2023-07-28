from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import RegistrationForm, LoginUserForm, CreateProfileForm, CreateLandlordProfileForm
from django.contrib.auth.hashers import make_password
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

        user = User(
            email=email, 
            password=make_password(password)
        )
        user.save()

        login(self.request, user)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    authentication_form = LoginUserForm
    redirect_authenticated_user = False

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)

class LogoutUserView(auth_views.LogoutView):
    pass


class CreateProfileView(FormView, PermissionRequiredMixin):
    """
    Creates a tenant profile
    """
    form_class = CreateProfileForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = User.objects.all()

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
            is_finished = True,
            profile_picture=profile_picture,
            user_id = user.last().pk
        )
        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)


class ChooseProfileView(TemplateView):
    template_name = 'choose_profile_type.html'


class CreateLandlordProfileView(FormView, PermissionRequiredMixin):
    form_class = CreateLandlordProfileForm
    template_name = 'create_landlord_profile.html'
    success_url = reverse_lazy('landlord_profile')

    def form_valid(self, form):
        user = User.objects.all()

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
            is_finished = True,
            type = type,
            user_id = user.last().pk
        )

        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)