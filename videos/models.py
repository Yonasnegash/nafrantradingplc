from django.db import models
from datetime import datetime

class VideoLocation(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self(title)

class Video(models.Model):
    name = models.CharField(max_length=100)
    video_upload = models.FileField(upload_to='videos/%Y/%m/%d/')
    video_url = models.CharField(max_length=1000)
    is_videoUrl = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    location = models.ForeignKey(VideoLocation, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self(name)
