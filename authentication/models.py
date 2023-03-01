from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber')
    )
    profile_photo = models.ImageField(blank=True, null=True)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            creators = Group.objects.get(name='creators')
            creators.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            subscribers = Group.objects.get(name='subscribers')
            subscribers.user_set.add(self)
