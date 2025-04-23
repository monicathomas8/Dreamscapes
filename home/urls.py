from django.urls import path
from . import views
from .views import contact_us, about

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_us, name='contact_us'),
    path('about/', about, name='about'),
]
