from .views import IndexView, ChooseYourProfile, DisplayProperties, RentOutPlace
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('all_properties', DisplayProperties.as_view(), name='all_properties'),
    path('rent_out', RentOutPlace.as_view(), name='rent_out')
]