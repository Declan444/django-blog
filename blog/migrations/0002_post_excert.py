# Generated by Django 4.2.14 on 2024-07-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="excert",
            field=models.TextField(blank=True),
        ),
    ]
