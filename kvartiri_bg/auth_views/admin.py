from django.contrib import admin
from .models import LandlordProfile, Profile, User


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(LandlordProfile)
class LandlordProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass