from django.contrib import admin
from .models import ArtistBio, ContactMessage

admin.site.register(ContactMessage)


@admin.register(ArtistBio)
class ArtistBioAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "updated_at", "background", "inspiration")
    search_fields = ("name", "user__username", "background", "inspiration")
    readonly_fields = ("updated_at",)
    fieldsets = (
        ("Basic Info", {
            "fields": (
                "user",
                "name",
                "profile_image"
                ),
        }),
        ("Artist Details", {
            "fields": (
                "background",
                "inspiration",
                "interests",
                "work_experience",
            ),
        }),
        ("Metadata", {
            "fields": ("updated_at",),
        }),
    )
