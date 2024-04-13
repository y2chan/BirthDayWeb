from django.db import models
from django.utils import timezone

class Message(models.Model):
    nickname = models.CharField(max_length=100)
    message = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photos/messages', default='')

    def __str__(self):
        return self.nickname

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description if self.description else "Photo"
