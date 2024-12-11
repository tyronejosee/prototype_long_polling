"""Views for Chat App."""

from time import sleep
from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime

from .models import Message


class ChatUpdatesView(APIView):
    def get(self, request, *args, **kwargs):
        last_check = request.GET.get("last_check", None)  # Client's timestamp
        if not last_check:
            return JsonResponse(
                {"error": "last_check parameter is required"}, status=400
            )

        # Convert the parameter to float (timestamp)
        last_check = float(last_check)
        for _ in range(30):  # Retry for 30 seconds
            new_messages = Message.objects.filter(
                timestamp__gt=datetime.fromtimestamp(last_check),
                is_read=False,
            )
            if new_messages.exists():
                messages = [
                    {
                        "id": msg.id,
                        "content": msg.content,
                        "timestamp": msg.timestamp.timestamp(),
                    }
                    for msg in new_messages
                ]
                return JsonResponse({"new_messages": messages}, status=200)
            sleep(10)  # Wait 1 second before retrying
        return JsonResponse({"message": "No updates"}, status=204)
