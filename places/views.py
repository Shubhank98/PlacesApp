from django.shortcuts import render

# Create your views here.
# places/views.py

from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer
from django.db import models

class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDeleteView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceSearchView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Place.objects.filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))
