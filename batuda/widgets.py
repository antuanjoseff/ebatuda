from django.contrib.gis.forms.widgets import BaseGeometryWidget

class CustomGeoWidget(BaseGeometryWidget):
    template_name = 'gis/custom_layers.html'
 