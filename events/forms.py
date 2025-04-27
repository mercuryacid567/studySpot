from django import forms
from .models import StudyEvent

class StudyEventForm(forms.ModelForm):
    class Meta:
        model = StudyEvent
        fields = ['title', 'description', 'location', 'time']
