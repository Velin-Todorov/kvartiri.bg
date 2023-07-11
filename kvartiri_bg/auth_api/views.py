from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class LoginView(View):
    form_class = SearchForm
    template_name = 'home.html'