from django.db import models
from djgeojson.fields import PointField
#from django.contrib.gis.db import models as gis_models


class SamplingStation(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    station_type = models.CharField(max_length=100)
    geom = PointField() #

    def __str__(self):
        return self.title
