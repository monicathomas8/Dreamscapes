from django.db import models
from django.utils.text import slugify


class Artwork(models.Model):
    """
    Model representing an artwork
    in the gallery with keywords
    for search functionality.
    """
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=False, null=False)
    keywords = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='artwork_images/')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Auto-generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
