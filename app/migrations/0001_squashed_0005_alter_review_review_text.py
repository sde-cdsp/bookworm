# Generated by Django 5.0.6 on 2024-06-25 13:26

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("app", "0001_initial"),
        ("app", "0002_remove_book_average_review_score"),
        ("app", "0003_alter_review_score"),
        ("app", "0004_alter_review_score"),
        ("app", "0005_alter_review_review_text"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
                ("pub_year", models.IntegerField(default=2024)),
                ("summary", models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                (
                    "score",
                    models.IntegerField(
                        default=0,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                ("review_text", models.CharField(max_length=500, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.book"
                    ),
                ),
            ],
        ),
    ]
