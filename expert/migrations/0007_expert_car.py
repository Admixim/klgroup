# Generated by Django 3.1.7 on 2021-12-02 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0015_auto_20211112_1225'),
        ('expert', '0006_expert_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='car',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expert_car', to='auto.car', verbose_name='ТС Заказчика'),
        ),
    ]
