from django.urls import path
from .views import CreateProperty, PropertyView, DeleteProperty, EditProperty, ReactToProperty, favourite_add, removed_favourite

urlpatterns = [
    path('create_property', CreateProperty.as_view(), name='create_property'),
    path('property/<int:pk>/', PropertyView.as_view(), name='property'),
    path('delete_property/<int:pk>/', DeleteProperty.as_view(), name="delete_property"),
    path('edit_property/<int:pk>', EditProperty.as_view(), name='edit_property'),
    path('react/property/<int:pk>', ReactToProperty.as_view(), name='react'),
    path('add_to_favourite/property/<int:pk>', favourite_add, name="add_to_favourite"),
    path('remove_from_favourite/property/<int:pk>', removed_favourite, name="remove favourite")
]
