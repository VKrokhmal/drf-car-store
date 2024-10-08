# Generated by Django 5.0.8 on 2024-08-21 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_alter_brand_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="odometer",
        ),
        migrations.RemoveField(
            model_name="car",
            name="price",
        ),
        migrations.CreateModel(
            name="CarLine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sku", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("odometer", models.PositiveIntegerField(default="0", null=True)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cars.car"
                    ),
                ),
            ],
            options={
                "verbose_name": "CarModel",
            },
        ),
    ]
