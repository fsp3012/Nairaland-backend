# Generated by Django 4.2.3 on 2023-07-27 17:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
