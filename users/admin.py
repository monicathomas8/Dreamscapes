from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_artist')
    search_fields = ('user__username', 'user__email')
    ordering = ('is_artist',)
