# Generated by Django 3.1.7 on 2022-03-22 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auto', '0015_auto_20211112_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.PositiveSmallIntegerField(
                    choices=[(1, 'ПТС'), (2, 'СТС'), (3, 'Договор КП'), (4, 'ОСАГО'), (5, 'КАСКО')])),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('scan_doc',
                 models.FileField(blank=True, default=None, null=True, upload_to='media/auto/', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.OneToOneField(blank=True, db_column='user', null=True,
                                                on_delete=django.db.models.deletion.CASCADE,
                                                to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Файл ТС',
                'verbose_name_plural': 'Файлы ТС',
            },
        ),
        migrations.RemoveField(
            model_name='car',
            name='doc_pass',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_date',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_datek',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_doc',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_dock',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_number',
        ),
        migrations.RemoveField(
            model_name='car',
            name='insurance_numberk',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AddField(
            model_name='autofiles',
            name='files',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='files_auto', to='auto.car', verbose_name='Прикрепленные файлы (Car)'),
        ),
    ]