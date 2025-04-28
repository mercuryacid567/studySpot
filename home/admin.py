from django.contrib import admin
from .models import Locations

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'spots', 'location', 'city', 'country', 'created_at')
    search_fields = ('name', 'city', 'country')
    list_filter = ('location', 'created_at')

admin.site.register(Locations, LocationsAdmin)