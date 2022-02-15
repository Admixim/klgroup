# Generated by Django 3.1.7 on 2021-06-29 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Марка ТС ')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Марка ТС',
                'verbose_name_plural': 'Марки ТС',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Модель ТС ')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.brend', verbose_name='Марка Авто')),
            ],
            options={
                'db_table': 'automarket_target_model',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Гос.номер ')),
                ('color', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Цвет')),
                ('date_made', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('sts', models.CharField(blank=True, default=None, max_length=11, null=True, verbose_name='Номер СТС')),
                ('sts_data', models.DateField(blank=True, default=None, null=True, verbose_name='Дата выдачи СТС')),
                ('pst', models.CharField(blank=True, default=None, max_length=11, null=True, verbose_name='Номер ПТС')),
                ('pts_data', models.DateField(blank=True, default=None, null=True, verbose_name='Дата выдачи ПТС')),
                ('vin', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='VIN номер')),
                ('insurance_number', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Номер полиса страхования ОСАГО')),
                ('insurance_date', models.DateField(blank=True, default=None, null=True, verbose_name='Дата выдачи полиса ОСАГО')),
                ('insurance_doc', models.FileField(blank=True, default=None, null=True, upload_to='upload/auto/insurance_osago/', verbose_name='Скан полиса ОСАГО')),
                ('insurance_numberk', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Номер полиса страхования КАСКО')),
                ('insurance_datek', models.DateField(blank=True, default=None, null=True, verbose_name='Дата выдачи полиса КАСКО')),
                ('insurance_dock', models.FileField(blank=True, default=None, null=True, upload_to='upload/auto/insurance_kasko/', verbose_name='Скан полиса КАСКО')),
                ('driver', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Сделать ссылку на клиента ')),
                ('doc_pass', models.FileField(blank=True, default=None, null=True, upload_to='upload/client/pasport/', verbose_name='Фото паспорта')),
                ('message', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('insurance_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_company', to='client.company', verbose_name='Страховая компания ОСАГО')),
                ('insurance_companyk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_companyk', to='client.company', verbose_name='Страховая компания КАСКО')),
                ('marka', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marka', to='auto.brend', verbose_name='Марка ')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='auto.model', verbose_name='Модель ')),
            ],
            options={
                'verbose_name': 'Транспортное средство  ',
                'verbose_name_plural': 'Транспортные средства',
                'ordering': ['-created'],
            },
        ),
    ]