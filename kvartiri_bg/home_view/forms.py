from django import forms
from .models import Property
from django.forms import RadioSelect

class SearchForm(forms.Form):
    """
    Form that handles searching for a property
    by town
    """
    town = forms.CharField()
    type = forms.ChoiceField(choices=Property.CHOICES)