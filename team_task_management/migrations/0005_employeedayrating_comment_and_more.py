# Generated by Django 4.1.1 on 2023-01-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_task_management', '0004_alter_employeedayrating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedayrating',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='employeedayrating',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
    ]
