# Generated by Django 4.1.7 on 2023-02-22 21:02
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
