# Generated by Django 3.2.23 on 2024-02-10 17:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20240204_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='avatar'),
        ),
    ]
