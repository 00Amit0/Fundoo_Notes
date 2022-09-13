from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=255)
    # email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField()
    location = models.CharField(max_length=200)


    class Meta:
        db_table = 'user'
