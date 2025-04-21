from django.urls import path
from .views import cart_view, checkout, remove_from_cart, order_list

urlpatterns = [
    path('cart/', cart_view, name='cart-view'),
    path('checkout/', checkout, name='checkout'),
    path('cart/remove/<int:artwork_id>/', remove_from_cart, name='remove-from-cart'),
    path('orders/', order_list, name='order-list'),
]
