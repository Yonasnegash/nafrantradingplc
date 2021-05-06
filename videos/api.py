from rest_framework import viewsets, permissions
from .models import Video, VideoLocation
from .serializers import VideoSerializer, VideoLocationSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoLocationViewSet(viewsets.ModelViewSet):
    queryset = VideoLocation.objects.all()
    serializer_class = VideoLocationSerializer