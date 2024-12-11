"""Models for Chat App."""

import uuid
from django.db import models
from django.utils.timezone import now


class Message(models.Model):
    """Model definition for Message."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now)
    is_read = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return self.content
