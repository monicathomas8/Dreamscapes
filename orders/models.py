from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """Order model to represent
    and manage a customer's order.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
    )

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    """
    OrderItem model to represent
    items within an order.
    """
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE
    )
    artwork = models.ForeignKey('artwork.Artwork', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
