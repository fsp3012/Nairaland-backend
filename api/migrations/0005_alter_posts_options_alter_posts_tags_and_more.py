# Generated by Django 4.2.3 on 2023-08-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_posts_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='posts',
            name='tags',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
