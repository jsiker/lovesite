from django.contrib import admin
from squish.models import Dater


#
# class DaterAdmin(admin.ModelAdmin):
#     list_display = ('username', 'age', 'gender')
#
#
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('city', 'country')


admin.site.register(Dater)
