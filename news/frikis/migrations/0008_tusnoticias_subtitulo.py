# Generated by Django 4.1.7 on 2023-04-08 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frikis', '0007_alter_tusnoticias_noticia_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tusnoticias',
            name='subtitulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
