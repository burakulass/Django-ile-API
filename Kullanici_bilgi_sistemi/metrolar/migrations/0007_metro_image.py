# Generated by Django 4.1 on 2022-08-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrolar", "0006_alter_metro_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="metro",
            name="image",
            field=models.ImageField(
                default="./static/img/Istanbul_Metro_Logo.svg.png", upload_to=""
            ),
        ),
    ]
