# Generated by Django 4.1 on 2022-08-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metrolar", "0002_metro_delete_makale"),
    ]

    operations = [
        migrations.RenameField(model_name="metro", old_name="id", new_name="Id",),
    ]
