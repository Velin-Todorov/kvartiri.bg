from django.forms.models import BaseModelForm
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginUserForm, CreateProfileForm
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Profile, User
# Create your views here


User = get_user_model()

class RegisterUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('finish_profile')
    
    def form_valid(self, form):
        return super().form_valid(form)  


    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm


class CreateProfileView(FormView, PermissionRequiredMixin):
    form_class = CreateProfileForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = User.objects.all()

        looking_for = form.cleaned_data['looking_for']
        about = form.cleaned_data['about']
        budget = form.cleaned_data['budget']
        profile_picture = form.cleaned_data['profile_picture']

        profile = Profile.objects.create(
            looking_for=looking_for,
            about=about,
            budget=budget,
            profile_picture=profile_picture,
            user_id = user.last().pk
        )
        return super().form_valid(form)  


    def form_invalid(self, form):
        print('Invalid')
        return super().form_invalid(form)



