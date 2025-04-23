from django.urls import path
from . import views
from .views import contact_us, about, email_signup

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_us, name='contact-us'),
    path('about/', about, name='about'),
    path('email-signup/', email_signup, name='email-signup'),
]
