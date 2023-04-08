# Generated by Django 4.1.7 on 2023-04-07 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frikis', '0005_alter_tusnoticias_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tusnoticias',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
