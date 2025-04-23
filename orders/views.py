from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from artwork.models import Artwork
from .models import Order, OrderItem
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

import stripe


@login_required
def order_list(request):
    """
    View to list all orders for
    the logged-in user.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})



def cart_view(request):
    """Displays the cart contents."""
    cart = request.session.get('cart', {})
    if not cart:
        request.session['cart'] = {}
        request.session.modified = True
    
    total_price = sum(float(item['price']) for item in cart.values())
    return render(request, 'orders/cart.html', {'cart': cart, 'total_price': total_price})


@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    """Processes checkout and creates an order."""

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart-view')

    total_price = sum(float(item['price']) for item in cart.values()) * 100

    payment_intent = stripe.PaymentIntent.create(
        amount=int(total_price),
        currency='gbp',
    )

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total_price / 100,
            status='Pending',
        )
        
        for artwork_id, item in cart.items():
            artwork = get_object_or_404(Artwork, id=artwork_id)
            OrderItem.objects.create(
                order=order,
                artwork=artwork,
                price=float(item['price']),
                quantity=1,
            )


        send_mail(
            subject='Order Confirmation - DreamScapes',
            message=f'Hi {request.user.username}, \n\nThank you for your order! Your order ID is {order.id}.',
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=[request.user.email],
            fail_silently=False,
        )
        request.session['cart'] = {}
        request.session.modified = True

        return redirect('thank-you')
    
    context = {
        'cart': cart,
        'total_price': total_price / 100,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': payment_intent.client_secret,
    }
    return render(request, 'orders/checkout.html', context)


def thank_you(request):
    return render(request, 'orders/thank_you.html')


def remove_from_cart(request, artwork_id):
    """
    Removes an artwork from
    the session-based cart.
    """
    cart = request.session.get('cart', {})

    if str(artwork_id) in cart:
        del cart[str(artwork_id)]
        messages.success(request, "Artwork removed from cart.")

    request.session['cart'] = cart  
    request.session.modified = True  

    return redirect('cart-view')


@login_required
def order_detail(request, order_id):
    """
    Displays the details
    of a specific order.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


def add_to_cart(request, artwork_id):
    """
    Add artwork to
    session based cart.
    """
    artwork = get_object_or_404(Artwork, id=artwork_id)
    cart = request.session.get('cart', {})

    if str(artwork_id) not in cart:
        cart[artwork_id] = {
            'title': artwork.title,
            'price': str(artwork.price),
            'image': artwork.image.url,
        }
        messages.success(request, f"{artwork.title} has been added to your cart.")
    else:
        messages.warning(request, f"{artwork.title} is already in your cart.")

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart-view')
