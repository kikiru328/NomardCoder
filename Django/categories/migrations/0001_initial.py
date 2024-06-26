# Generated by Django 5.0.6 on 2024-05-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("uploadted_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "kind",
                    models.CharField(
                        choices=[("rooms", "Rooms"), ("experiences", "Experiences")],
                        max_length=15,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
