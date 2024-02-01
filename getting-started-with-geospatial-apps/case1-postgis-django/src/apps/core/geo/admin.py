from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WorldBorder

class WorldBorderAdmin(OSMGeoAdmin):
    list_display = ("name", "region", "subregion", "lon", "lat")
    list_filter = ("region", "subregion")
    search_fields = ("name",)

admin.site.register(WorldBorder, WorldBorderAdmin)

