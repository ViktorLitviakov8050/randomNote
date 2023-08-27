from django.db import models

# Create your models here.

from django.db import models
from uuid import uuid4


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, unique=True)
    token = models.UUIDField(unique=True, default=uuid4)
    created = models.DateTimeField(auto_now_add=True)
