from django.urls import path
from . import views
from .views import (
    cart_view,
    checkout,
    remove_from_cart,
    order_list,
    order_detail,
)

urlpatterns = [
    path(
        'add-to-cart/<int:artwork_id>/',
        views.add_to_cart,
        name='add-to-cart',
    ),
    path('cart/', cart_view, name='cart-view'),
    path('shipping-info/', views.shipping_info, name='shipping-info'),
    path('payment/', views.checkout_payment, name='checkout-payment'),
    path('checkout/', checkout, name='checkout'),
    path(
        'cart/remove/<int:artwork_id>/',
        remove_from_cart,
        name='remove-from-cart',
    ),
    path('orders/', order_list, name='order-list'),
    path('orders/<int:order_id>/', order_detail, name='order-detail'),
    path('thank-you/', views.thank_you, name='thank-you'),
]
