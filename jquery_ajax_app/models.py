from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order-detail", kwargs={'pk': self.pk})


