# Generated by Django 3.1.7 on 2022-03-16 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('client', '0017_auto_20220316_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileperson',
            name='files_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='files_persons', to='client.client',
                                    verbose_name='Прикрепленные файлы (Client)'),
        ),
    ]
