from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """Order model to represent
    and manage a customer's order.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])


class OrderItem(models.Model):
    """
    OrderItem model to represent
    items within an order.
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    artwork = models.ForeignKey('artwork.Artwork', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
