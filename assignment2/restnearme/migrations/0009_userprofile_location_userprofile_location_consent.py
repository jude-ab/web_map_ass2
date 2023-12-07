# Generated by Django 4.2.5 on 2023-12-07 00:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restnearme', '0008_michelinrestaurants_cuisine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location_consent',
            field=models.BooleanField(default=False),
        ),
    ]
