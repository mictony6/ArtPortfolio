# Generated by Django 4.0.4 on 2022-06-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_artwork_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
