from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    user_type = models.CharField(max_length=5)