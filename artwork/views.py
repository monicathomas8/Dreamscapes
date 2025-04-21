from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Artwork


# --- Artwork Views ---
class ArtworkListView(ListView):
    """
    View for displaying a list
    of all artwork enteries.
    """
    model = Artwork
    template_name = "artwork_list.html"
    context_object_name = "artworks"
    ordering = ['title']


class ArtworkDetailView(DetailView):
    """
    View for displaying a
    single artwork entry.
    """
    model = Artwork
    template_name = "artwork_detail.html"
    context_object_name = "artwork"


# --- Add to cart ---


def add_to_cart(request, artwork_id):
    """
    Add artwork to
    session based cart.
    """
    artwork = get_object_or_404(Artwork, id=artwork_id)
    cart = request.session.get('cart', {})
    cart[artwork_id] = {
        'title': artwork.title,
        'price': str(artwork.price),
        'image': artwork.image.url,
    }

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart-view')
