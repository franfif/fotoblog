from django.conf import settings
from django.db import models


class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
