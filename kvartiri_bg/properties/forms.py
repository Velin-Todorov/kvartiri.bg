from django import forms
from django.db import models
from .models import Property, Picture, MessageFromTenant


class CreateProperty(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'type',
            'price_per_month',
            'size',
            'town',
            'address',
            'about',
            'images',
            'furnished',
            'utilities_included'
        ]

class ChangePictures(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture']
        widgets = {'picture': forms.FileInput()}



class ReactionForm(forms.ModelForm):
    class Meta:
        model = MessageFromTenant
        fields = ['msg_content']
        widget = {
            'sender': forms.TextInput()
        }
