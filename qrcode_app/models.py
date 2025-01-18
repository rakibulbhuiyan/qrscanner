
from django.db import models

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class CardForm(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=255)
    review_link = models.URLField()

    def __str__(self):
        return f"Form submitted by {self.name}"
