from django.urls import path
from . import views
from .views import (
    create_custom_order,
    user_dashboard,
    edit_order,
    delete_order,
)

urlpatterns = [
    path('custom-order/', create_custom_order, name='create-custom-order'),
    path('dashboard/', user_dashboard, name='user-dashboard'),
    path('order/edit/<int:order_id>/', edit_order, name='edit-order'),
    path('order/delete/<int:order_id>/', delete_order, name='delete-order'),
    path('update-profile/', views.update_profile, name='update_profile'),

]
