from django.db import models
from .constants import CHOICES, PRICE_RANGE, TYPE, PROFILE_TYPE
from home_view.models import Property
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, UserManager, User
from datetime import datetime, timezone
# Create your models here.



User._meta.get_field('email')._unique = True
# class CustomUserManager(UserManager):
#     pass


# class User(AbstractUser, PermissionsMixin):
#     """
#     Custom User model
#     """
#     email = models.EmailField(unique=True)
#     username=models.TextField(blank=True, null=True)
#     type = models.CharField(choices=PROFILE_TYPE, max_length=11, default=PROFILE_TYPE[0][0])
#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['type']


from django.conf import settings
class Profile(models.Model):
    """
    Model that contains app-specific info about the user
    """
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    looking_for = models.CharField(choices=CHOICES, max_length=11, blank=False)
    about = models.TextField(blank=True)
    is_finished = models.BooleanField(default=False)
    budget = models.CharField(choices=PRICE_RANGE, max_length=18, blank=False, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    is_verified = models.BooleanField(default=False)
    saved_properties = models.ForeignKey(Property, null=True, blank=True, on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics/')


class LandlordProfile(models.Model):
    """
    Model that contains app-specific info about the landlord
    """
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True)
    is_finished = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    offerings = models.ForeignKey(Property, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE, max_length=15, default=TYPE[0][0])
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        current_datetime = datetime.now()
        return (current_datetime - self.created_at).days

  
