from django.urls import path
from .views import create_custom_order, user_dashboard

urlpatterns = [
    path('custom-order/', create_custom_order, name='create-custom-order'),
    path('dashboard/', user_dashboard, name='user-dashboard')
]
