# Generated by Django 4.2.5 on 2023-12-06 23:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restnearme', '0003_alter_michelinrestaurants_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='michelinrestaurants',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
