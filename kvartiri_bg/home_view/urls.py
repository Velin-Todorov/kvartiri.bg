from .views import IndexView, DisplayProperties, RentOutPlace, AboutPage, HowToUseIt
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('all_properties', DisplayProperties.as_view(), name='all_properties'),
    path('rent_out', RentOutPlace.as_view(), name='rent_out'),
    path('about', AboutPage.as_view(), name='about'),
    path('how_does_it_work', HowToUseIt.as_view(), name='how_does_it_work')
]