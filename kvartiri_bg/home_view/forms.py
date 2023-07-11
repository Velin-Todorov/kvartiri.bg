from django import forms
from .models import Property
from django.forms import RadioSelect

from consts import CITIES


class SearchForm(forms.Form):
    """
    Form that handles searching for a property
    by town
    """
    town = forms.ChoiceField(choices=CITIES, initial=CITIES[0])
    type = forms.ChoiceField(choices=Property.CHOICES)