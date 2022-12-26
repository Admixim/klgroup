# Generated by Django 3.1.7 on 2022-06-26 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Таблица ')),
                ('comment', models.CharField(blank=True, default=None, max_length=3000, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Модель БД ',
                'verbose_name_plural': 'Модели БД',
            },
        ),
        migrations.CreateModel(
            name='Document_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Наименование ')),
                ('tags', models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='Тэг')),
                ('model', models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='Поле модели')),
                ('comment', models.CharField(blank=True, default=None, max_length=3000, null=True, verbose_name='Комментарий ')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('table', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='document.table', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Список тэгов в шаблоне',
                'verbose_name_plural': 'Список тэгов в шаблоне',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Название документа ')),
                ('location', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Местоположение ')),
                ('author', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Автор документа')),
                ('customer', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Заказчик ')),
                ('comment', models.CharField(blank=True, default=None, max_length=3000, null=True, verbose_name='Комментарий ')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('executor', models.ForeignKey(blank=True, default=None, max_length=30, on_delete=django.db.models.deletion.CASCADE, to='client.company', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Body_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Название объекта  док')),
                ('text', models.TextField(blank=True, default=None, max_length=10000, null=True, verbose_name='Поле объекта док ')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='document.document', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'поле документа',
                'verbose_name_plural': 'поля документа',
            },
        ),
    ]
