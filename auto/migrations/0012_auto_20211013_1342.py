# Generated by Django 3.1.7 on 2021-10-13 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0011_auto_20211013_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='doc_pass',
            new_name='scan_doc',
        ),
    ]