from .views import IndexView, ChooseYourProfile
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='home')
]