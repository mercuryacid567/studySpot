from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from events.models import StudyEvent


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    #get study events created by the user
    created_events = StudyEvent.objects.filter(created_by=request.user).order_by('-time')

    #get study events that the user has joined
    joined_events = StudyEvent.objects.filter(participants=request.user).exclude(created_by=request.user).order_by(
        '-time')

    if request.method == 'POST':
        username = request.POST.get('username')
        bio = request.POST.get('bio')

        if username and username != request.user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            else:
                request.user.username = username
                request.user.save()
                messages.success(request, 'Username updated successfully.')

        if bio is not None:
            profile.bio = bio

        if 'profileImage' in request.FILES:
            profile.profile_pic = request.FILES['profileImage']

        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')

    context = {
        'profile': profile,
        'user': request.user,
        'created_events': created_events,
        'joined_events': joined_events,
    }
    return render(request, 'user_profile/profile.html', context)