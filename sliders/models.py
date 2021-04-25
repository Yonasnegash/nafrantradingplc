from django.db import models
from datetime import datetime

class Slider(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    picture_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    picture_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    picture_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    picture_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    picture_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    is_created = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self(name)


