from typing import Any, Dict
from auth_views.models import LandlordProfile, Profile
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator
from functools import wraps

class GetContextBasedOnType:
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        if self.request.user.is_authenticated:
            if self.request.user.type == 'LANDLORD':
                context['landlord'] = LandlordProfile.objects.get(user_id=self.request.user.pk)
            else:
                context['profile'] = Profile.objects.get(user_id=self.request.user.pk)

        return context

class UserContextMixin:

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['user'] = self.request.user
            return context
        
class SuccessMixin:
    def get_success_url(self) -> str:
        if self.request.user.type == 'TENANT':
            return reverse('profile', kwargs={'pk':Profile.objects.get(user_id = self.request.user.pk).pk})
        else:
            return reverse('landlord_profile', kwargs={'pk':LandlordProfile.objects.get(user_id = self.request.user.pk).pk})
        


def tenant_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.type == 'TENANT':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('You cannot access this page!')
    
    return _wrapped_view

def landlord_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.type == 'LANDLORD':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('You cannot access this page!')
    
    return _wrapped_view


class TenantOnlyMixin:
    @method_decorator(tenant_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    
class LandlordOnlyMixin:
    @method_decorator(landlord_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

