from django.shortcuts import render
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


def about_us(request):
    """
    Render the about us page.
    """
    return render(request, 'home/about_us.html')


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
