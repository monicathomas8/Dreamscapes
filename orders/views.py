from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Order


@login_required
def order_list(request):
    """
    View to list all orders for
    the logged-in user.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
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

    # Create an order for the user
    order = Order.objects.create(
        user=request.user,
        total_price=sum(float(item['price']) for item in cart.values()),
        status='Pending',
        )

    # Convert cart items into order items
    for artwork_id, item in cart.items():
        artwork = get_object_or_404(Artwork, id=artwork_id)
        OrderItem.objects.create(
            order=order,
            artwork=artwork,
            price=float(item['price']),
            quantity=1,
            )

    # Clear the cart after checkout
    request.session['cart'] = {}
    request.session.modified = True

    return redirect('order-list')


@login_required
def remove_from_cart(request, artwork_id):
    """
    Removes an artwork from
    the session-based cart.
    """
    cart = request.session.get('cart', {})

    if artwork_id in cart:
        del cart[artwork_id]  

    request.session['cart'] = cart  
    request.session.modified = True  

    return redirect('cart-view')  
