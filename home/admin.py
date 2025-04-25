from django.contrib import admin
from .models import ArtistBio


@admin.register(ArtistBio)
class ArtistBioAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "updated_at")
    search_fields = ("name", "user__username")
