from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ChooseYourProfile(TemplateView):
    template_name = 'pre_register.html'
        
