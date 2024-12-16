from django.contrib.auth.models import User
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_available = models.IntegerField()
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)

    def __str__(self):
        return self.name

