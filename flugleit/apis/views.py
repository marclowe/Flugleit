from django.shortcuts import render

# apis/views.py
from rest_framework import generics
from rest_framework import viewsets

from accounts import models
from accounts import models
from .serializers import FlugleitSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = models.Flight.objects.all()
    serializer_class = FlugleitSerializer


# class DetailFlight(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Flight.objects.all()
#     serializer_class = FlugleitSerializer