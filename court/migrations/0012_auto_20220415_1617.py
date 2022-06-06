# Generated by Django 3.1.7 on 2022-04-15 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0011_auto_20220415_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='date_start',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Начало исполнения С'),
        ),
        migrations.AlterField(
            model_name='court',
            name='date_stop',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Завершения исполнения С'),
        ),
    ]