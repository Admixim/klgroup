# Generated by Django 3.1.7 on 2022-04-12 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0008_auto_20211209_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='info_court',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info_courts', to='court.infocourt', verbose_name='Список юр.оперций '),
        ),
    ]