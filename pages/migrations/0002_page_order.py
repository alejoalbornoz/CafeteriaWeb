# Generated by Django 5.1.2 on 2024-11-08 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="order",
            field=models.SmallIntegerField(default=0),
        ),
    ]