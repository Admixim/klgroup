# Generated by Django 3.1.7 on 2022-05-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0019_auto_20220530_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autofiles',
            name='scan_doc',
            field=models.FileField(upload_to='media/auto/', verbose_name='Файл'),
        ),
    ]