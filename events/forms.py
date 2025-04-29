from django import forms
from .models import StudyEvent

class StudyEventForm(forms.ModelForm):
    class Meta:
        model = StudyEvent
        fields = ['title', 'location', 'time', 'spots', 'address', 'vibe']
