# Generated by Django 4.1.7 on 2023-04-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frikis', '0004_tusnoticias_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tusnoticias',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
