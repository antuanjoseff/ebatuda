from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    gang = models.CharField(max_length=25, blank=True)
    

class HuntingRaid(models.Model):
    code = models.CharField(max_length=255, primary_key=True)
    date = models.DateField()
    geom = models.MultiPolygonField(spatial_index=False, null=True, blank=True)
    

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Àrea privada de caça'
        verbose_name_plural = 'Àrees privades de caça'