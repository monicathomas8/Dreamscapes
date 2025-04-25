from django.shortcuts import render, redirect
from .models import ArtistBio
from .forms import ArtistBioForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    """
    Render the home page.
    """
    return render(request, 'home/index.html')


def contact_us(request):
    """
    Render the contact us page.
    """
    return render(request, 'home/contact_us.html')


def about(request):
    """
    Render the about us page.
    """
    return render(request, 'home/about.html')


def email_signup(request):
    """
    Handle email signup form submission.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            #  save the email to a database or send a confirmation email
            messages.success(request, 'Thank you for signing up!')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return render(request, 'home/email_signup.html')


@login_required
def update_bio(request):
    """
    Update the artist bio for the logged-in user.
    """
    bio, created = ArtistBio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ArtistBioForm(request.POST, request.FILES, instance=bio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your bio has been updated!')
            return redirect('about')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ArtistBioForm(instance=bio)
    return render(request, 'home/update_bio.html', {'form': form})
