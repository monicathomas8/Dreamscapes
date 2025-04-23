from django.urls import path
from .views import ArtworkListView, ArtworkDetailView, add_to_cart

urlpatterns = [
    path('', ArtworkListView.as_view(), name='artwork-list'),
    path('<slug:slug>/', ArtworkDetailView.as_view(), name='artwork-detail'),
    path('artwork/add-to-cart/<int:artwork_id>/', add_to_cart, name='add-to-cart'),
    path('add-to-cart/<int:artwork_id>/', add_to_cart, name='add-to-cart'),
]
