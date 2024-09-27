from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User_O(models.Model):
    user_id = models.CharField(max_length=20)
    email = models.EmailField()
    timestamp = models.DateTimeField()
    tasks = models.JSONField()

    def __str__(self):
        return self.user_id
