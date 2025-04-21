from django.contrib import admin
from .models import Artwork


class ArtworkAdmin(admin.ModelAdmin):
    """
    Admin interface for Artwork model."""
    prepopulated_fields = {"slug": ("title",)}  # Auto-generate slug in admin
    fields = ('title', 'slug', 'description', 'image', 'price', 'keywords')


admin.site.register(Artwork, ArtworkAdmin)
# Register the Artwork model with the custom admin interface
