# Generated by Django 3.1.7 on 2021-12-07 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0005_remove_infocourt_accident'),
        ('accident', '0012_auto_20211201_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='court_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='court_info', to='court.infocourt', verbose_name='Инфо о Судопроизводстве'),
        ),
    ]