# Generated by Django 5.0.1 on 2024-01-26 19:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "userprofile",
            "0005_rename_premiun_days_has_finish_userprofile_premiun_days_selected_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="day_for_premiun_use",
            new_name="days_for_premiun_use",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="premiun_days_selected",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="tests_days_selected",
        ),
    ]
