from django import forms
from .models import Property
from django.forms import RadioSelect, widgets

from consts import CITIES


class SearchForm(forms.Form):
    """
    Form that handles searching for a property
    by town
    """
    town = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control me-2', 'type': 'search', 'placeholder': 'Search...', 'aria-label': 'Search'}
        ), label='')