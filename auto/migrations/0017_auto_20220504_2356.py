# Generated by Django 3.1.7 on 2022-05-04 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0016_auto_20220322_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autofiles',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files_auto', to='auto.car', verbose_name='Прикрепленные файлы (Car)'),
        ),
        migrations.AlterField(
            model_name='autofiles',
            name='scan_doc',
            field=models.FileField(upload_to='media/auto/', verbose_name='Файл'),
        ),
    ]