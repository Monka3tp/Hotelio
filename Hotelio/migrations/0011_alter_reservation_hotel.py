# Generated by Django 4.2.17 on 2025-01-11 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotelio', '0010_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='Hotelio.hotel'),
        ),
    ]
