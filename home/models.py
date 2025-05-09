from datetime import datetime
from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=500)
    spots = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime(2025, 1, 1, 12, 0))
    location = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    lat = models.CharField(max_length=200, blank=True, null=True)
    lng = models.CharField(max_length=200, blank=True, null=True)
    place_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name