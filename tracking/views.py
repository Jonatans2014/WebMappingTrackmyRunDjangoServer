from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework.filters import DjangoFilterBackend
from rest_framework_gis.filters import *
from rest_framework_gis.pagination import GeoJsonPagination

from  .models import Location
from .serializers import LocationGeoSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class SnippetList(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationGeoSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationGeoSerializer


class GeojsonLocationList(RetrieveAPIView):
    model = Location
    queryset = Location.objects.all()
    serializer_class = LocationGeoSerializer



geojson_location_list = GeojsonLocationList.as_view()