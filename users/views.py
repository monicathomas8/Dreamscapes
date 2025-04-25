from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, CustomOrderForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomOrder
from orders.models import Order


def signup(request):
    """
    View to handle user signup.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def create_custom_order(request):
    """
    View to create a custom order.
    Only accessible to logged-in users.
    """
    if request.method == "POST":
        form = CustomOrderForm(request.POST)
        if form.is_valid():
            custom_order = form.save(commit=False)
            custom_order.user = request.user

            custom_order.save()
            messages.success(request, "Your custom order has been submitted!")
            return redirect('home')
        else:
            messages.error(
                request,
                "There was an error with your submission. Please try again."
            )
    else:
        form = CustomOrderForm()

    return render(request, 'users/create_custom_order.html', {'form': form})


@login_required
def user_dashboard(request):
    """
    View for users to manage past cart
    orders and custom orders.
    Only accessible to logged-in users.
    """
    custom_orders = CustomOrder.objects.filter(user=request.user)
    past_cart_orders = Order.objects.filter(
        user=request.user).order_by('-created_at')
    
    return render(request, 'users/dashboard.html', {
        'custom_orders': custom_orders,
        'past_cart_orders': past_cart_orders,
    })


@login_required
def edit_order(request, order_id):
    """
    View to edit a custom order.
    Only accessible to logged-in users.
    """
    order = get_object_or_404(CustomOrder, id=order_id, user=request.user)

    if request.method == 'POST':
        form = CustomOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Custom order updated successfully!')
            return redirect('user-dashboard')
    else:
        form = CustomOrderForm(instance=order)

    return render(request, 'users/edit_order.html', {'form': form})


@login_required
def delete_order(request, order_id):
    """
    View to delete a custom order.
    Only accessible to logged-in users.
    """
    order = get_object_or_404(CustomOrder, id=order_id, user=request.user)

    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Custom order deleted successfully!')
        return redirect('user-dashboard')

    return render(request, 'users/delete_order.html', {'order': order})


@login_required
def update_profile(request):
    """
    View to update user profile information.
    Only accessible to logged-in users.
    """
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard')

    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'users/update_profile.html', {'form': form})
