from django.shortcuts import render
from django.core.serializers import serialize
from .models import HuntingRaid
from django.http import JsonResponse
import json

# Create your views here.
def get_batudes(request):
    data = serialize("geojson", HuntingRaid.objects.all(), geometry_field="geom", fields=["code"])
    return JsonResponse(json.loads(data), safe=False)