from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    TrackID = models.CharField(max_length=50)
    LatLong = models.LineStringField()



    def __str__(self):
        return self.TrackID