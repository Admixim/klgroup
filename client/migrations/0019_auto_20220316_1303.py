# Generated by Django 3.1.7 on 2022-03-16 06:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('client', '0018_auto_20220316_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileperson',
            old_name='files_person',
            new_name='files_persons',
        ),
    ]
