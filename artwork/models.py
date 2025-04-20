from django.db import models


class Artwork(models.Model):
    """
    Model representing an artwork
    in the gallery with keywords
    for search functionality.
    """
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    keywords = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='artwork_images/')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
        )


def __str__(self):
    return self.title
