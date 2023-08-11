from typing import Any, Dict
from auth_views.models import LandlordProfile, Profile
from django.urls import reverse

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