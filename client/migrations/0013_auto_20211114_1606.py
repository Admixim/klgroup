# Generated by Django 3.1.7 on 2021-11-14 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0010_auto_20211114_1606'),
        ('client', '0012_auto_20211114_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_client', to='accident.status', verbose_name='Статус в ДТП  '),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
