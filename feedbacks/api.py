from feedbacks.models import Feedback
from rest_framework import viewsets, permissions
from .serializers import FeedbackSerializer

# Feedback viewset
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = FeedbackSerializer