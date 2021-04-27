from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)