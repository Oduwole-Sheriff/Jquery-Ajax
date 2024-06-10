from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)