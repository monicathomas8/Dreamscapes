from django.contrib import admin
from .models import UserProfile, CustomOrder


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for UserProfile model.
    """
    list_display = ('user', 'is_artist')
    search_fields = ('user__username', 'user__email')
    list_editable = ('is_artist',)
    ordering = ('is_artist', 'user')


@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    """
    Admin interface for CustomOrder model.
    """
    list_display = (
        'id',
        'user',
        'description',
        'size',
        'colours',
        'theme',
        'style',
        'extra_suggestions',
        'contact_email'
    )
    list_filter = ('theme', 'created_at', 'updated_at')
    search_fields = ('user__username', 'discription', 'contat_email')
