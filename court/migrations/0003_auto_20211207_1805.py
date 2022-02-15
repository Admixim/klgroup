# Generated by Django 3.1.7 on 2021-12-07 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0012_auto_20211201_1445'),
        ('court', '0002_auto_20211114_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='court',
            options={'ordering': ['-created'], 'verbose_name': 'Оперция судопроизводства', 'verbose_name_plural': 'Оперции судопроизводства'},
        ),
        migrations.AlterModelOptions(
            name='listend',
            options={'ordering': ['-created'], 'verbose_name': 'Список окончания сроков вступления в силу ', 'verbose_name_plural': 'Списки окончания сроков вступления в силу'},
        ),
        migrations.RemoveField(
            model_name='court',
            name='court',
        ),
        migrations.AddField(
            model_name='infocourt',
            name='accident',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='court_accident', to='accident.accident', verbose_name='Судебная информация'),
        ),
        migrations.AddField(
            model_name='infocourt',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='court_status', to='court.status', verbose_name='Статус  дела'),
        ),
    ]