from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=15, unique=True)
    video_title = models.CharField(max_length=50)
    channel_id = models.CharField(max_length=25)
    channel_title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    published_at = models.DateTimeField(max_length=20)
    thumbnail = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['video_title']),
            models.Index(fields=['description']),
        ]
        ordering = ['-published_at']

    def __str__(self):
        return self.video_title
    
    
