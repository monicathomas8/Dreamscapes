from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from artwork.models import Artwork
from .models import Order, OrderItem
from django.contrib import messages


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
    total_price = sum(float(item['price']) for item in cart.values())
    return render(request, 'orders/cart.html', {'cart': cart, 'total_price': total_price})


@login_required
def checkout(request):
    """Processes checkout and creates an order."""
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart-view')


    total_price=sum(float(item['price']) for item in cart.values())

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
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

        return redirect('order-list')
    return render(request, 'orders/checkout.html', {'cart': cart, 'total_price': total_price})



def remove_from_cart(request, artwork_id):
    """
    Removes an artwork from
    the session-based cart.
    """
    cart = request.session.get('cart', {})

    if str(artwork_id) in cart:
        del cart[str(artwork_id)]  

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

