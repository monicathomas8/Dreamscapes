from django.urls import path
from .views import cart_view, checkout, order_list

urlpatterns = [
    path('cart/', cart_view, name='cart-view'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', order_list, name='order-list'),
]
