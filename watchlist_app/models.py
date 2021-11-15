from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.ImageField(upload_to='icons')
    
    def __str__(self):
        return self.name


class WatchList(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    IsActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
