from django.contrib import admin
from .models import LandlordProfile, Profile, User


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name']
    list_filter = ['location']

@admin.register(LandlordProfile)
class LandlordProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name']
    list_filter = ['location']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass