from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User


@login_required
def profile_view(request):
    # Get or create profile for the current user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        bio = request.POST.get('bio')

        # Update username if changed
        if username and username != request.user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            else:
                request.user.username = username
                request.user.save()
                messages.success(request, 'Username updated successfully.')

        # Update bio
        if bio is not None:
            profile.bio = bio

        # Update profile picture
        if 'profileImage' in request.FILES:
            profile.profile_pic = request.FILES['profileImage']

        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')

    context = {
        'profile': profile,
        'user': request.user,
    }
    return render(request, 'user_profile/profile.html', context)