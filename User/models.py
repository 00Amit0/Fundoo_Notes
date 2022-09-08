from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField()
    location = models.CharField(max_length=200)
