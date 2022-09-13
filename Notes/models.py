from django.db import models
from User.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)


    class Meta:
        db_table = 'notes'

