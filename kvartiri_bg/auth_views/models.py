from django.db import models
from .constants import CHOICES, PRICE_RANGE
from home_view.models import Property
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, UserManager, User
# Create your models here.


class CustomUserManager(UserManager):
    pass


class User(AbstractUser, PermissionsMixin):
    """
    Custom User model
    """
    username= None
    email = models.EmailField(unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


from django.conf import settings
class Profile(models.Model):
    """
    Model that contains app-specific info about the user
    """
    looking_for = models.CharField(choices=CHOICES, max_length=11, blank=False, null=True)
    about = models.TextField(blank=True, null=True)
    budget = models.CharField(choices=PRICE_RANGE, max_length=18, blank=False, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    is_verified = models.BooleanField(default=False)
    saved_properties = models.ForeignKey(Property, null=True, blank=True, on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    USERNAME_FIELD = 'email'