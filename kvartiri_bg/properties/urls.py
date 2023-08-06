from django.urls import path
from .views import CreateProperty, PropertyView

urlpatterns = [
    path('create_property', CreateProperty.as_view(), name='create_property'),
    path('property/<int:pk>/', PropertyView.as_view(), name='property')
]
