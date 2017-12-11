from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from .models import Location
from django.contrib.gis.geos import Point

from rest_framework import pagination, serializers
from rest_framework_gis import serializers as gis_serializers




class LocationGeoSerializer(GeoFeatureModelSerializer):
    """ location geo serializer  """


    class Meta:
        model = Location
        geo_field = "LatLong"
        fields = ('TrackID','LatLong')
