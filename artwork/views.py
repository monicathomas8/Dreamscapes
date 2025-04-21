from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Artwork


class ArtworkListView(ListView):
    """ View for displaying a list
    of all artwork enteries.
    """
    model = Artwork
    template_name = "artwork_list.html"


class ArtworkDetailView(DetailView):
    """ View for displaying a
    single artwork entry.
    """
    model = Artwork
    template_name = "artwork_detail.html"
