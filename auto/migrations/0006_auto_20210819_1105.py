# Generated by Django 3.1.7 on 2021-08-19 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_auto_20210812_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='message',
            new_name='Comment',
        ),
    ]