# Generated by Django 3.1.7 on 2021-11-12 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0014_car_human'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='human',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_company',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_companyk',
        ),
    ]