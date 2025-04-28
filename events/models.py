from django.db import models
from django.contrib.auth.models import User
from home.models import Locations

# Create your models here.

class StudyEvent(models.Model):
    location_object = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    time = models.DateTimeField()
    spots = models.IntegerField(default=10)
    address = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    participants = models.ManyToManyField(User, related_name='joined_events')

    def save(self, *args, **kwargs):
        creating = self.pk is None  # Check if this is a new StudyEvent
        super().save(*args, **kwargs)

        # If this is a brand new StudyEvent, create matching Location
        if creating:
            new_location = Locations.objects.create(
                name=self.title,
                location=self.location,
                time=self.time,
                spots=self.spots,
                zipcode = "30332",
                city="Atlanta",
                country="USA",
                address=self.address,
            )
            self.location_object = new_location  # Link the new location
            super().save(update_fields=['location_object'])