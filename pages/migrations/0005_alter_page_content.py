# Generated by Django 5.1.2 on 2024-11-09 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_alter_page_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=models.TextField(),
        ),
    ]