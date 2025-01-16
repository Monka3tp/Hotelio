from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='media/hotel_images', default='media/hotel_images/hotelrelax.jpeg')
    image2 = models.ImageField(upload_to='media/hotel_images', default='media/hotel_images/hotelrelax.jpeg')
    image3 = models.ImageField(upload_to='media/hotel_images', default='media/hotel_images/hotelrelax.jpeg')
    image4 = models.ImageField(upload_to='media/hotel_images', default='media/hotel_images/hotelrelax.jpeg')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    amenities = models.TextField(default="brak udogodnień")
    rating = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, null=True, blank=True)
    map = models.URLField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    promo = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    review_text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

