from django.db import models
from .constants import CHOICES, PRICE_RANGE, TYPE, PROFILE_TYPE, OCCUPATION
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, UserManager
from datetime import datetime
from properties.consts import bulgarian_cities
from django.contrib.auth.hashers import make_password

# Create your models here.


class CustomUserManager(UserManager):

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )

        password = make_password(password) 
        user.set_password(password) #make password
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(AbstractUser, PermissionsMixin):
    """
    Custom User model
    """
    email = models.EmailField(unique=True)
    username = None
    type = models.CharField(choices=PROFILE_TYPE, max_length=11, default=PROFILE_TYPE[0][0])
    profile_finished = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class LandlordProfile(models.Model):
    """
    Model that contains app-specific info about the landlord
    """
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True)
    location = models.TextField(choices=bulgarian_cities, max_length=20, blank=False, default=bulgarian_cities[0][0])
    profile_finished = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    type = models.CharField(choices=TYPE, max_length=15, default=TYPE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        current_datetime = datetime.now()
        return (current_datetime - self.created_at).days

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    """
    Model that contains app-specific info about the user
    """
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    looking_for = models.CharField(choices=CHOICES, max_length=11, blank=False, default=CHOICES[0][0])
    phone_number = models.TextField(blank=True, null=True)
    location = models.TextField(choices=bulgarian_cities, max_length=20, blank=False, default=bulgarian_cities[0][0])
    about = models.TextField(blank=True)
    profile_finished = models.BooleanField(default=False)
    budget = models.CharField(choices=PRICE_RANGE, max_length=18, blank=False, null=True, default=PRICE_RANGE[0][0])
    current_occupation = models.CharField(choices=OCCUPATION, max_length=15, default=OCCUPATION[0][0])
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')

    USERNAME_FIELD = 'email'


