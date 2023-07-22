from django.forms.models import BaseModelForm
from django.views import generic as views
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import RegistrationForm, LoginUserForm
from django.contrib.auth import views as auth_views, login, get_user_model
# Create your views here.


UserModel = get_user_model()

class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        result =  super().form_valid(form)

        login(self.request, self.object)

        return result

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context
    

    def get_success_url(self):

        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm



