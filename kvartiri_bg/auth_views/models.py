from django.db import models
from home_view.models import Property
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
# Create your models here.


class CustomAccountManager(BaseUserManager):
    """
    Custom Account Manager
    """
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, first_name, last_name, email, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, last_name=last_name, 
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save(commit=True)
        return user


class User(AbstractUser, PermissionsMixin):
    """
    Custom User model
    """
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'password1',
        'password2' 
    ]

class UserProfile(models.Model):
    """
    Model that contains app-specific info about the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_premium = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    saved_properties = models.ForeignKey(Property, null=True, blank=True, on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)