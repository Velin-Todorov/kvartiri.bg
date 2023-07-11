from home_view.models import User
from django import forms
from rest_framework import serializers

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password']
        

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password']