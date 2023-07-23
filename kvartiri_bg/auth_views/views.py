from django.forms.models import BaseModelForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import User

from .forms import RegistrationForm, LoginUserForm
from django.contrib.auth import views as auth_views, login, get_user_model
# Create your views here


# class OnlyAnonymousMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponse(self.get_success_url())

#         return super().dispatch(request, *args, **kwargs)


class RegisterUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm



