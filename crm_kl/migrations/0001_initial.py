# Generated by Django 3.1.7 on 2021-11-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='order_site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Имя Фамилия')),
                ('message', models.CharField(blank=True, default=None, max_length=5000, null=True, verbose_name='Цель обращения')),
                ('contact', models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='Контактный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Заявки сайт ',
                'verbose_name_plural': 'Заявки сайт',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Имя Фамилия')),
                ('contact', models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='Контактный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
                ('service', models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='Интересующая услуга')),
                ('message', models.CharField(blank=True, default=None, max_length=5000, null=True, verbose_name='Цель обращения')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Вопросы сайт ',
                'verbose_name_plural': 'Вопросы сайт',
                'ordering': ['-created'],
            },
        ),
    ]
