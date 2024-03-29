# Generated by Django 4.1.7 on 2023-03-08 14:52
import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Picture",
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
                ("title", models.CharField(blank=True, default="", max_length=150)),
                (
                    "picture",
                    models.ImageField(
                        max_length=150,
                        upload_to="uploaded/%Y/%m",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png"]
                            )
                        ],
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-uploaded_at"],
            },
        ),
    ]
