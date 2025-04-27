from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudyEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    participants = models.ManyToManyField(User, related_name='joined_events')

    def __str__(self):
        return self.title