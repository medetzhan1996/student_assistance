# Generated by Django 4.1 on 2023-02-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0011_alter_demandcompletedfile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='demanddistribution',
            name='payment',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Оплачено'), (2, 'Неоплачено')], default=2),
        ),
    ]