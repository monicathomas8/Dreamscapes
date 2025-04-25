from django.shortcuts import render, redirect
from .forms import SignupForm, CustomOrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomOrder


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
