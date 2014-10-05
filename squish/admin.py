from django.contrib import admin
from squish.models import Dater, Location

admin.site.register(Dater)
admin.site.register(Location)

class DaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')