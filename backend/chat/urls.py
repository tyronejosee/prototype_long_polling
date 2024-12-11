"""Urls for Chat App."""

from django.urls import path

from .views import ChatUpdatesView


urlpatterns: list = [
    path(
        "chat-updates/",
        ChatUpdatesView.as_view(),
        name="chat-updates",
    ),
]
