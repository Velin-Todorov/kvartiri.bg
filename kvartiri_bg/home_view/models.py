from django.db import models
from django_select2 import forms as s2forms

# Create your models here.


class Town(models.Model):
    """
    A model for a town in Bulgaria
    """
    name = models.TextField()


class Property(models.Model):
    """
    This is a model for a room 
    of any type - studio, single room, appartment
    """

    STUDIO: tuple = 'STUDIO', 'Studio'
    APPARTMENT: tuple = 'APPARTMENT', 'Appartment'
    ROOM: tuple = 'SINGLE_ROOM', 'Single Room'

    CHOICES = [
        STUDIO,
        APPARTMENT,
        ROOM
    ]

    size = models.IntegerField()
    type = models.CharField(choices=CHOICES, max_length=11)
    price_per_month = models.DecimalField(max_digits=20, decimal_places=2)
    landlord = models.TextField()
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    street = models.TextField()
    street_number = models.IntegerField()
    floor = models.IntegerField(blank=True, null=True, default=0)
    area_postcode = models.IntegerField()
    availability = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    furnished = models.BooleanField()
    utilities_included = models.BooleanField()


class Landlord(models.Model):
    pass


class User(models.Model):
    pass


class Townidget(s2forms.ModelSelect2Widget):
    search_fields = [
        ''
    ]
