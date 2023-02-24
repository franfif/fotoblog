from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    DEFAULT_PROFILE_PHOTO = 'Portrait_placeholder.png'

    ROLE_CHOICES = (
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber')
    )
    profile_photo = models.ImageField(
        default=DEFAULT_PROFILE_PHOTO)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
