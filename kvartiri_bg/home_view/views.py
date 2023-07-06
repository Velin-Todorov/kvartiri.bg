from django.shortcuts import render
from django.views.generic import View
from .forms import SearchForm

# Create your views here.
class IndexView(View):
    form_class = SearchForm
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        """
        GET
        Method that renders the home page
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})