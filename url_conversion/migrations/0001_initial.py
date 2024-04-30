# Generated by Django 5.0.4 on 2024-04-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URLShortener",
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
                ("original_url", models.URLField(max_length=100, unique=True)),
                ("shorten_url", models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
