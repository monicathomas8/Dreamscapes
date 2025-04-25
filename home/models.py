from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ArtistBio(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="artist_bio"
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Enter your Artist name."
    )
    interests = models.TextField(
        blank=True,
        help_text="List your artistic interests."
    )
    background = models.TextField(help_text="Tell your story as an artist.")
    inspiration = models.TextField(
        blank=False,
        null=False,
        help_text="What inspires your work?"
    )
    work_experience = models.TextField(
        blank=True,
        help_text="Share your past projects or exhibitions."
    )
    profile_image = CloudinaryField('image', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Bio"
