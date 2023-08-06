from django import forms
from django.db import models
from .models import Property, Picture


class CreateProperty(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'type',
            'price_per_month',
            'size',
            'town',
            'address',
            'images',
            'furnished',
            'utilities_included'
        ]

