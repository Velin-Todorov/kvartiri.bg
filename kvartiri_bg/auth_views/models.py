from django.db import models
from .constants import CHOICES
from home_view.models import Property
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, UserManager
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

class UserProfile(models.Model):
    """
    Model that contains app-specific info about the user
    """
    username  = None
    looking_for = models.CharField(choices=CHOICES, max_length=11, blank=True, null=True)
    budget = models.ValueRange(start=0, end=100000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_premium = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    saved_properties = models.ForeignKey(Property, null=True, blank=True, on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(blank=True)

    USERNAME_FIELD = User.email