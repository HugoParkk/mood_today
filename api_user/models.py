from django.db import models

# Create your models here.
class User(models.Model):
    email = models.TextField()
    password = models.TextField()
    username = models.TextField()