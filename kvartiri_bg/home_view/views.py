from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'

class ChooseYourProfile(TemplateView):
    template_name = 'pre_register.html'
        
