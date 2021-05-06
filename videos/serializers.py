from rest_framework import serializers
from .models import Video, VideoLocation

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class VideoLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLocation
        fields = '__all__'