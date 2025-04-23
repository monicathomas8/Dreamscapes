from django.shortcuts import render


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

