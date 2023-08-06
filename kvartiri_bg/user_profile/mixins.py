from django.urls import reverse
from auth_views.models import Profile, LandlordProfile

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