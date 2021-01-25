from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    date_of_birth = models.DateField(blank=True,null=True)
    password = models.CharField(max_length=100)
    file = models.FileField(blank=True,upload_to='images/')

    def __str__(self):
        return self.username
