from django.contrib.gis import admin
from .models import WorldBorder
from leaflet.admin import LeafletGeoAdmin


admin.site.register(WorldBorder, LeafletGeoAdmin)