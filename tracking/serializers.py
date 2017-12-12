from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from .models import location
from django.contrib.gis.geos import Point

from rest_framework import pagination, serializers
from rest_framework_gis import serializers as gis_serializers




class LocationGeoSerializer(GeoFeatureModelSerializer):
    """ location geo serializer  """

    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = location
        geo_field = "latlong"
        fields = ('trackID','latlong','distance','time','images')




