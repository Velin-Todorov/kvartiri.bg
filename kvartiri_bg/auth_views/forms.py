from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.forms import ModelForm
from .models import Profile
from .constants import CHOICES, PRICE_RANGE


UserModel = get_user_model()

class LoginUserForm(auth_forms.AuthenticationForm):
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'relative block w-full rounded-t-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-100 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
                'placeholder': 'Email Address'
            }
        )
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'elative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-100 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
                'placeholder': 'Password'
            }
        )
    )
        

class RegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'relative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-100 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'relative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-100 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
                    'placeholder': 'Last Name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'relative block w-full rounded-t-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-100 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
                    'placeholder': 'Email Address'
                }
            )
        }   


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['looking_for', 'about', 'budget', 'profile_picture']
        widgets = {
            'looking_for': forms.RadioSelect(choices=CHOICES),
            'budget': forms.RadioSelect(choices=PRICE_RANGE)
        }
    