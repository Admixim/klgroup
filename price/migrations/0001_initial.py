# Generated by Django 3.1.7 on 2021-11-15 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0015_auto_20211114_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Номенклатура')),
                ('price', models.IntegerField(blank=True, default=None, verbose_name='Цена')),
                ('extra_charge', models.IntegerField(blank=True, default=None, verbose_name='Наценка')),
                ('comment', models.CharField(blank=True, default=None, max_length=2000, verbose_name='Комментарий')),
                ('date', models.DateField(blank=True, default=None, null=True, verbose_name='Дата  актуален ')),
                ('code_name', models.CharField(blank=True, default=None, max_length=400, verbose_name='Тэг')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Прайс услуг ',
                'verbose_name_plural': 'Прайсы услуг',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, default=None, max_length=2000, verbose_name='Номер договора')),
                ('date', models.DateField(blank=True, default=None, null=True, verbose_name='Дата заключения ')),
                ('name', models.CharField(blank=True, default=None, max_length=200, verbose_name='Наименование')),
                ('summa', models.IntegerField(blank=True, default=None, verbose_name='Сумма договора')),
                ('comment', models.CharField(blank=True, default=None, max_length=7000, verbose_name='Коментарий')),
                ('contract_pdf', models.FileField(blank=True, default=None, null=True, upload_to='upload/price/', verbose_name='Файл договора')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_contract', to='client.company', verbose_name='Организация')),
                ('contragent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contragent_contract', to='client.company', verbose_name='Контрагент')),
            ],
            options={
                'verbose_name': 'Договор  ',
                'verbose_name_plural': 'Договора ',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Bank_pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True, verbose_name='Сумма Контракта')),
                ('pay_number', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Номер платежки')),
                ('pay_date', models.DateField(blank=True, default=None, null=True, verbose_name='Дата платежа ')),
                ('bank_pay_pdf', models.FileField(blank=True, default=None, null=True, upload_to='upload/price/', verbose_name='Файл платежки')),
                ('comment', models.CharField(blank=True, default=None, max_length=2000, null=True, verbose_name='Комментарий')),
                ('date_create', models.DateField(blank=True, default=None, null=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_pay', to='client.company', verbose_name='Страхователь  ')),
            ],
            options={
                'verbose_name': 'Платеж по цессии  ',
                'verbose_name_plural': 'Платежи по цессиям ',
                'ordering': ['-created'],
            },
        ),
    ]