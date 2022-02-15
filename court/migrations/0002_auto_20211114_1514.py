# Generated by Django 3.1.7 on 2021-11-14 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Судья Ф.И.О. ')),
                ('adress_mail', models.EmailField(blank=True, default=None, max_length=300, null=True, verbose_name='Электронный адрес ')),
                ('contact_phone', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Контактный телефон ')),
                ('message', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Судья фамилия ',
                'verbose_name_plural': 'Судьи фамилии',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='judge_help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Помошник судьи  ФИО')),
                ('message', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Помошник судьи ',
                'verbose_name_plural': 'Помошники судей',
                'ordering': ['-created'],
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
                'verbose_name': 'Статус  судебной оперции',
                'verbose_name_plural': 'Статусы судебных операций',
            },
        ),
        migrations.CreateModel(
            name='ListCourt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Наименование суда ')),
                ('adress', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Адрес Суда ')),
                ('adress_post', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Почтовый адрес ')),
                ('adress_mail', models.EmailField(blank=True, default=None, max_length=300, null=True, verbose_name='Электронный адрес ')),
                ('contact_phone', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Контактный телефон ')),
                ('message', models.CharField(blank=True, default=None, max_length=2000, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('judge', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='judge', to='court.judge', verbose_name='Судья Ф.И.О. ')),
                ('judge_help', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='judge_help1', to='court.judge_help', verbose_name='Секретарь судьи ')),
            ],
            options={
                'verbose_name': 'Справочник судебных участков ',
                'verbose_name_plural': 'Справочник судебных участков',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='judge',
            name='judge_help',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='judge_help', to='court.judge_help', verbose_name='Секретарь судьи '),
        ),
        migrations.CreateModel(
            name='InfoCourt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Номер Судебного дела')),
                ('uid_number', models.CharField(blank=True, default=None, max_length=26, null=True, verbose_name='УИД Судебного дела')),
                ('data_reg', models.DateField(blank=True, default=None, null=True, verbose_name='Дата регистрации дела')),
                ('message', models.CharField(blank=True, default=None, max_length=2000, null=True, verbose_name='Результат события Коментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='court.listcourt', verbose_name='Место  ')),
            ],
            options={
                'verbose_name': 'Информация дела',
                'verbose_name_plural': 'Информация дела',
                'ordering': ['-created'],
            },
        ),
    ]