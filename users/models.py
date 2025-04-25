from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Enter your name"
    )
    is_artist = models.BooleanField(
        default=False,
        help_text="Check if the user is an artist"
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"


class CustomOrder(models.Model):
    """
    Model to handle custom orders for artists.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='custom_orders'
        )
    description = models.TextField(
        help_text="Description of the custom order in detail"
    )
    size = models.CharField(
        max_length=50,
        help_text="Size of the artwork (e.g., A4, A3, etc.)"
    )
    colours = models.CharField(
        max_length=255,
        help_text="Preferred colours for the artwork"
    )
    theme = models.CharField(
        max_length=255,
        help_text="Theme of the artwork (e.g., nature, abstract, etc.)"
    )
    style = models.CharField(
        max_length=255,
        help_text=(
            "Preferred style of the artwork "
            "(e.g., realism, impressionism, etc.)"
        )
    )
    extra_suggestions = models.TextField(
        blank=True,
        help_text="Any extra suggestions, requirments or notes for the artist"
    )
    contact_email = models.EmailField(
        help_text="Email address for the artist to contact the user"
    )
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return (
            f"Custom Order #{self.id} by {self.user.username} on "
            f"{self.created_at.strftime('%Y-%m-%d')}"
        )
