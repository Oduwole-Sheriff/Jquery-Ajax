from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
