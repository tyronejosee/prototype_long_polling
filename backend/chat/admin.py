"""Admin configs for Chat App."""

from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin for Message model."""

    list_display: list[str] = ["id", "content", "timestamp", "is_read", "is_available"]
    list_filter: list[str] = ["is_read", "is_available", "timestamp"]
    search_fields: list[str] = ["content"]
    ordering: list[str] = ["-timestamp"]
    readonly_fields: list[str] = ["id", "timestamp"]
