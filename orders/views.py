from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import stripe
from artwork.models import Artwork
from .models import Order, OrderItem
from django.core.mail import send_mail
from .forms import DeliveryAddressForm


stripe.api_key = settings.STRIPE_SECRET_KEY


def add_to_cart(request, artwork_id):
    """Add artwork to session-based cart."""
    artwork = get_object_or_404(Artwork, id=artwork_id)
    cart = request.session.get('cart', {})

    if str(artwork_id) not in cart:
        cart[artwork_id] = {
            'title': artwork.title,
            'price': str(artwork.price),
            'image': artwork.image.url,
        }
        messages.success(
            request, f"{artwork.title} has been added to your cart."
        )
    else:
        messages.warning(request, f"{artwork.title} is already in your cart.")

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart-view')


def remove_from_cart(request, artwork_id):
    """Remove an artwork from the session-based cart."""
    cart = request.session.get('cart', {})

    if str(artwork_id) in cart:
        del cart[str(artwork_id)]
        messages.success(request, "Artwork removed from cart.")

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart-view')


def cart_view(request):
    """Displays the cart contents."""
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) for item in cart.values())

    return render(request, 'orders/cart.html', {
        'cart': cart,
        'total_price': total_price,
    })


@login_required
def checkout(request):
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


@login_required
def thank_you(request):
    """Display the thank-you page with
    download links and collect delivery details."""
    latest_order = Order.objects.filter(user=request.user) \
        .order_by('-created_at').first()

    if latest_order and latest_order.status == 'Pending':
        latest_order.status = 'Completed'
        latest_order.save()

        message = (
            f"Hi {request.user.username},\n\n"
            f"Thank you for your order!\n\n"
            f"Order ID: {latest_order.id}\n"
            f"Total Price: £{latest_order.total_price}\n\n"
            "We hope you enjoy your purchase!\n\n"
            "You will receive a separate email"
            "with delivery details once your "
            "artwork has been dispatched.\n\n"
            "artwork has been dispatched.\n\n"
            "If you have any questions, feel free to reach out to us.\n\n"
            "Best regards,\n"
            "DreamScapes Team"
        )
        send_mail(
            subject='Order Confirmation - DreamScapes',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
            fail_silently=False,
        )

    if request.method == 'POST':
        address_form = DeliveryAddressForm(request.POST)
        if address_form.is_valid():
            delivery_data = address_form.cleaned_data
            request.session['delivery_data'] = delivery_data
            messages.success(request, "Delivery details saved successfully!")
            return redirect('order-list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        address_form = DeliveryAddressForm()

    return render(request, 'orders/thank_you.html', {
        "latest_order": latest_order,
        "address_form": address_form,
    })


@login_required
def order_list(request):
    """View to list all orders for the logged-in user."""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Displays the details of a specific order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
