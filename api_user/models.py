from django.db import models


# Create your models here.
class User(models.Model):
    email = models.TextField(primary_key=True)
    password = models.TextField()
    username = models.TextField()

    class Meta:
        db_table = "User"
