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
