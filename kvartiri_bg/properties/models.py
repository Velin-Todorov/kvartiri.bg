from django.db import models
from auth_views.constants import CHOICES
from .consts import bulgarian_cities, YES_NO
from auth_views.models import LandlordProfile, Profile
from django.apps import apps

# Create your models here.

class Property(models.Model):
    """
    Model that represents a Property of different type
    """
  
    type = models.CharField(choices=CHOICES, default='ROOM', max_length=15)
    price_per_month = models.DecimalField(max_digits=20, decimal_places=2)
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE, null=True, blank=True)
    about = models.TextField()
    liked_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    size = models.IntegerField()
    town = models.CharField(choices=bulgarian_cities, blank=True, max_length=15, default=bulgarian_cities[0][0]) #dropdown field
    address = models.TextField()
    images = models.ImageField(upload_to='property_pics', blank=True, null=True)
    furnished = models.CharField(choices=YES_NO, max_length=3, null=True, default=YES_NO[0][0])
    utilities_included = models.CharField(choices=YES_NO, max_length=3, null=True, default=YES_NO[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Picture(models.Model):
    picture = models.ImageField(upload_to='media/property_pics')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
