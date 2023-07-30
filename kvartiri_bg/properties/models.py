from django.db import models
from auth_views.constants import CHOICES
from auth_views.models import LandlordProfile

# Create your models here.
class Property(models.Model):
    """
    Model that represents a Property of different type
    """
    type = models.CharField(choices=CHOICES, default='ROOM', max_length=15)
    price_per_month = models.DecimalField(max_digits=20, decimal_places=2)
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    size = models.IntegerField()
    town = models.CharField(blank=True, max_length=15) #dropdown field
    address = models.TextField()
    furnished = models.BooleanField()
    utilities_included = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


