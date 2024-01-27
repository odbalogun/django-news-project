from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    age = models.PositiveIntegerField(null=True, blank=True)
