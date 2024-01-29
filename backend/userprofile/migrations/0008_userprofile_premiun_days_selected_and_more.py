# Generated by Django 5.0.1 on 2024-01-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "userprofile",
            "0007_rename_days_for_premiun_use_userprofile_start_date_for_premiun_use_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="premiun_days_selected",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="tests_days_selected",
            field=models.BooleanField(default=False),
        ),
    ]