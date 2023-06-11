from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = None
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

