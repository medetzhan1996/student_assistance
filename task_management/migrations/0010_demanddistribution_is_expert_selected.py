# Generated by Django 3.2.13 on 2023-01-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0009_auto_20230130_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='demanddistribution',
            name='is_expert_selected',
            field=models.BooleanField(default=False),
        ),
    ]
