# Generated by Django 3.1.7 on 2021-12-03 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0007_expert_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Вид')),
                ('comment', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Вид экспертизы',
                'verbose_name_plural': 'Виды экспертизы',
            },
        ),
        migrations.AddField(
            model_name='expert',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expert_type', to='expert.type', verbose_name='Вид экспертизы'),
        ),
    ]
