from django.shortcuts import render, redirect, get_object_or_404
from .models import StudyEvent
from .forms import StudyEventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def study_spots_home(request):
    events = StudyEvent.objects.all()
    return render(request, 'events/study_spots_home.html', {'events': events})

@login_required
def create_study_event(request):
    if request.method == 'POST':
        form = StudyEventForm(request.POST)
        if form.is_valid():
            study_event = form.save(commit=False)
            study_event.created_by = request.user
            study_event.save()
            return redirect('events.home')
    else:
        form = StudyEventForm()
    return render(request, 'events/create_study_event.html', {'form': form})

@login_required
def join_study_event(request, event_id):
    event = get_object_or_404(StudyEvent, id=event_id)
    event.participants.add(request.user)
    return redirect('events.home')