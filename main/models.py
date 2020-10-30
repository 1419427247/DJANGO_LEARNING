from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):

    name=models.CharField(max_length=32)

    password=models.CharField(max_length=128)

    registration_data=models.DateTimeField(default=timezone.now)

    cookie=models.CharField(max_length=128)

    

    def __str__(self):
        return self.name
