# Generated by Django 4.1.4 on 2023-01-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_developer",
            field=models.BooleanField(default=False),
        ),
    ]
