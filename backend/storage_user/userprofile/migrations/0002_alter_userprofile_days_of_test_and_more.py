# Generated by Django 5.0.1 on 2024-01-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="days_of_test",
            field=models.PositiveIntegerField(default=15, max_length=2),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="days_of_use_as_premiun",
            field=models.PositiveIntegerField(default=30, max_length=2),
        ),
    ]
