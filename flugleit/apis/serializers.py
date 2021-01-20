from rest_framework import serializers
from accounts import models

class FlugleitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'flightday',
            'carrierfscode', 
            'flightnumber',
            'departureairportfscode', 
            'formatteddeparture', 
            'arrivalairportfscode',
            'formattedarrival', 
            'edit',
            'flightequipmentiatacode',
            'id'
        )
        model = models.Flight