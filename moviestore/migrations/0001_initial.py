# Generated by Django 5.0.7 on 2024-07-30 21:27

import django.core.validators
import moviestore.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Director",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        null=True,
                        upload_to="moviestore/images",
                        validators=[moviestore.validators.validate_file_size],
                    ),
                ),
                ("release_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "G"),
                            ("PG", "PG"),
                            ("PG-13", "PG-13"),
                            ("R", "R"),
                            ("NC-17", "NC-17"),
                        ],
                        default="G",
                        max_length=5,
                    ),
                ),
                (
                    "score",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("Genre", models.ManyToManyField(to="moviestore.genre")),
                ("actors", models.ManyToManyField(to="moviestore.actor")),
                ("director", models.ManyToManyField(to="moviestore.director")),
            ],
        ),
    ]
