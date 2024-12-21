from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='hotel_images/', default='hotel_images/hotelrelax.jpeg')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    amenities = models.TextField(default="brak udogodnień")
    rating = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, null=True, blank=True)
    map_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    review_text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"

