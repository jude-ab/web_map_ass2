# Generated by Django 4.2.5 on 2023-12-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restnearme', '0005_alter_michelinrestaurants_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='michelinrestaurants',
            name='city',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
