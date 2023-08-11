from django.contrib import admin
from .models import Property, MessageFromLandlord, MessageFromTenant

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('type', 'landlord', 'size', 'town')
    list_filter = ('town')
    ordering = ('created_at')
    sortable_by = ('price_per_month')


    