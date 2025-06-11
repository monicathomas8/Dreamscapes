from django.shortcuts import render, redirect
from .models import ArtistBio
from .forms import ArtistBioForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    """
    Render the home page.
    """
    return render(request, 'home/index.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                ("Thank you for your message! "
                 "We'll be in touch soon.")
            )
            return redirect('contact-us')
    else:
        form = ContactForm()

    return render(request, 'home/contact_us.html', {'form': form})


def about(request):
    """
    Render the about us page
    with artist information.
    """
    artist = ArtistBio.objects.first()
    context = {
        'artist': artist,
        }

    return render(request, 'home/about.html', context)


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
    Checks if user is marked as an artist.
    """
    user_profile = request.user.profile
    if not user_profile.is_artist:
        messages.error(request, 'You must be an artist to update your bio.')
        return redirect('home')

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


def faq(request):
    """FAQ page view."""
    return render(request, 'home/faq.html')
