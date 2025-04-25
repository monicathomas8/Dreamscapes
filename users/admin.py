from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for UserProfile model.
    """
    list_display = ('user', 'is_artist')
    search_fields = ('user__username', 'user__email')
    list_editable = ('is_artist',)
    ordering = ('is_artist', 'user')
