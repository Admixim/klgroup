# Generated by Django 3.1.7 on 2021-12-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0004_court_info_court'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infocourt',
            name='accident',
        ),
    ]
