# Generated by Django 5.1.2 on 2024-11-06 00:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(related_name="get_posts", to="blog.category"),
        ),
        migrations.AlterField(
            model_name="post",
            name="published",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
