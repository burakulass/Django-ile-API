# Generated by Django 4.1 on 2022-08-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrolar", "0014_alter_hastane_latitude_alter_hastane_longitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hastane", name="Latitude", field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="hastane", name="Longitude", field=models.FloatField(),
        ),
    ]
