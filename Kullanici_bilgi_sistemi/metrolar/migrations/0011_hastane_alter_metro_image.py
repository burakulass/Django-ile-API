# Generated by Django 4.1 on 2022-08-24 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrolar", "0010_delete_metro1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hastane",
            fields=[
                ("_id", models.IntegerField(primary_key=True, serialize=False)),
                ("ADI", models.CharField(max_length=150)),
                ("ILCE_ADI", models.IntegerField()),
                ("ACIL_SERVIS", models.BooleanField(default=True)),
                ("AMBULANS", models.BooleanField(default=True)),
                ("Longitude", models.CharField(max_length=120)),
                ("Latitude", models.CharField(max_length=120)),
            ],
            options={"db_table": "Hastane",},
        ),
        migrations.AlterField(
            model_name="metro",
            name="image",
            field=models.ImageField(
                default="./static/img/Istanbul_Metro_Logo.svg.png",
                upload_to="img/%Y/%m/%d/",
            ),
        ),
    ]