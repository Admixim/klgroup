# Generated by Django 3.1.7 on 2022-05-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_auto_20220530_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecompany',
            name='scan_doc',
            field=models.FileField(default=None, null=True, upload_to='media/company/', verbose_name='Файл'),
        ),
    ]
