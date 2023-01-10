# Generated by Django 3.1.7 on 2022-06-26 09:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('court', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Тип документа')),
                ('full_name', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Полное наименование')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Док основание  ДТП',
                'verbose_name_plural': 'Док основание  ДТП',
            },
        ),
        migrations.CreateModel(
            name='AccidentPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Тип документа')),
                ('full_name', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Полное наименование')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Док опеределение ДТП',
                'verbose_name_plural': 'Док определение ДТП',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Наименование')),
                ('comment', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статус  дела о ДТП',
                'verbose_name_plural': 'Статусы дела о ДТП',
            },
        ),
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, default=None, null=True, verbose_name='Дата ДТП ')),
                ('time', models.TimeField(blank=True, default=None, null=True, verbose_name='Время ДТП ')),
                ('location_accident', models.CharField(blank=True, default=None, max_length=400, verbose_name='Место ДТП')),
                ('number', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Номер протокола')),
                ('file_doc', models.FileField(blank=True, default=None, null=True, upload_to='upload/protokol_doc/', verbose_name='Файл Основание')),
                ('file_pos', models.FileField(blank=True, default=None, null=True, upload_to='upload/protokol_pos/', verbose_name='Файл Постановление')),
                ('data_insurance', models.DateField(blank=True, default=None, null=True, verbose_name='Дата обращения в Страховую')),
                ('message', models.CharField(blank=True, default=None, max_length=100000, null=True, verbose_name='Комментарий')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('court_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='court_info', to='court.infocourt', verbose_name='Инфо о Судопроизводстве')),
                ('dtp_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dtp_doc', to='accident.accidentdoc', verbose_name='Документ Основание ')),
                ('dtp_pos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AccidentPos', to='accident.accidentpos', verbose_name='Документ Постановление ')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_acc', to='accident.status', verbose_name='Статус  дела о ДТП')),
            ],
            options={
                'verbose_name': 'ДТП  ',
                'verbose_name_plural': 'ДТП',
                'ordering': ['-created'],
            },
        ),
    ]