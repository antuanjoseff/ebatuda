# from django.contrib import admin
from django.contrib.gis import admin
from django.contrib.gis.forms.widgets import OSMWidget
from .models import HuntingRaid
from .widgets import CustomGeoWidget

class CustomGeoWidget(OSMWidget):
    template_name = 'gis/custom_layers.html'
    

class CustomGeoModelAdmin(admin.GISModelAdmin): 
    gis_widget = CustomGeoWidget 

# Register your models here.
@admin.register(HuntingRaid)
class ApcAdmin(CustomGeoModelAdmin):

    pass