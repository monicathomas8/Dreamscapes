from django.urls import path
from .views import create_custom_order

urlpatterns = [
    path('custom-order/', create_custom_order, name='create-custom-order'),
]
