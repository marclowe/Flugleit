# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

class Flight(models.Model):
    flightday = models.CharField(max_length=50, default = '')
    carrierfscode = models.CharField(max_length=50)
    flightnumber = models.CharField(max_length=50)
    departureairportfscode = models.CharField(max_length=50)
    formatteddeparture = models.CharField(max_length=50)
    arrivalairportfscode = models.CharField(max_length=50)
    formattedarrival = models.CharField (max_length=50)
    flightequipmentiatacode = models.CharField (max_length=50, default = '')
    edit = models.BooleanField(default = False)

    def __str__(self):
       return 
