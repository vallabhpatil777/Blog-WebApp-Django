# Generated by Django 5.1.4 on 2024-12-11 20:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_postmodel_date_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="postmodel",
            options={"ordering": ("-date_created",)},
        ),
    ]
