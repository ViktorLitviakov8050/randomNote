from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    token = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
