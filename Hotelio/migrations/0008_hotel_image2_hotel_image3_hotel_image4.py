# Generated by Django 4.2.17 on 2025-01-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotelio', '0007_hotel_sale_price_alter_hotel_promo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image2',
            field=models.ImageField(default='media/hotel_images/hotelrelax.jpeg', upload_to='media/hotel_images'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='image3',
            field=models.ImageField(default='media/hotel_images/hotelrelax.jpeg', upload_to='media/hotel_images'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='image4',
            field=models.ImageField(default='media/hotel_images/hotelrelax.jpeg', upload_to='media/hotel_images'),
        ),
    ]