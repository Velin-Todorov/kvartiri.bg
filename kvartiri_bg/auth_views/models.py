from django.db import models
from django.contrib.auth import models as auth_models
from home_view.models import Property
# Create your models here.


class User(auth_models.AbstractUser):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    is_premium = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    saved_properties = models.ForeignKey(Property, null=True, blank=True, on_delete=models.SET_NULL)
    profile_picture = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result