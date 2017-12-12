from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class location(models.Model):
    """
    A model which holds information about a particular location
    """
    trackID = models.CharField(max_length=50)
    latlong = models.LineStringField()
    distance = models.CharField(max_length=50,default=0)
    time = models.CharField(max_length=50, default="00:00")



    def __str__(self):
        return self.trackID



class image(models.Model):

    track = models.ForeignKey(location, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(max_length=100)



    def __str__(self):
        return '%s' '%s' % (self.track, self.images)