from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    TrackID = models.CharField(max_length=50)
    LatLong = models.LineStringField()
    distance = models.CharField(max_length=50,default=0)
    time = models.CharField(max_length=50, default="00:00")


    def __str__(self):
        return self.TrackID


