# Generated by Django 3.1.7 on 2022-06-26 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto', '0001_initial'),
        ('accident', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя ')),
                ('surname', models.CharField(blank=True, max_length=24, null=True, verbose_name='Фамилия ')),
                ('midlename', models.CharField(blank=True, max_length=24, null=True, verbose_name='Отчество ')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона')),
                ('phone2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона 1')),
                ('serial_pass', models.CharField(blank=True, help_text='Вводится 4 цифры без пробела', max_length=5, null=True, verbose_name='Серия паспорта')),
                ('number_pass', models.IntegerField(blank=True, help_text='Вводится 6 цифр без пробела', null=True, verbose_name='Номер паспорта')),
                ('enter_org', models.CharField(blank=True, help_text='УВД,ОВД,ЗАГС, МВД', max_length=100, null=True, verbose_name='Кем выдан')),
                ('data_create', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('adress_reg', models.CharField(blank=True, max_length=50, verbose_name='Место регистрации')),
                ('adress_home', models.CharField(blank=True, max_length=50, verbose_name='Место жительства')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('point_birth', models.CharField(blank=True, max_length=50, verbose_name='Место рождение')),
                ('doc_pass', models.FileField(blank=True, default=None, upload_to='client/upload/pasport/', verbose_name='Фото паспорта')),
                ('serial_lic', models.CharField(blank=True, default=None, help_text='Вводится 4 цифры без пробела', max_length=24, null=True, verbose_name='Серия ВУ')),
                ('number_lic', models.CharField(blank=True, default=None, help_text='Вводится 6 цифр без пробела', max_length=100, null=True, verbose_name='Номер ВУ')),
                ('enter_lic', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Кем выдан ГИБДД')),
                ('create_lic', models.DateField(blank=True, default=None, null=True, verbose_name='Дата  выдачи')),
                ('adress_lic', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Место выдачи ВУ')),
                ('category', models.CharField(blank=True, default=None, help_text='B,C,D,E,BC,DE,A', max_length=50, null=True, verbose_name='Категории прав')),
                ('doc_lic', models.FileField(blank=True, default=None, null=True, upload_to='assets/img/products_images/', verbose_name='Фото ВУ')),
                ('post_mail', models.EmailField(blank=True, max_length=24, null=True, verbose_name='Адрес Эл.почты')),
                ('link_social', models.URLField(blank=True, default=None, max_length=24, null=True, verbose_name='Адрес в соц.сети')),
                ('attorney', models.DateField(blank=True, default=None, null=True, verbose_name='Дата  Окончание доверенности')),
                ('doc_attorney', models.FileField(blank=True, default=None, null=True, upload_to='upload/doc_attorney/', verbose_name='Файл Доверенности')),
                ('doc_requisites', models.FileField(blank=True, default=None, null=True, upload_to='upload/doc_requisites/', verbose_name='Файл Реквизитов банк')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Клиент  ',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Название компании')),
                ('full_name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Полное наименование компании')),
                ('nalog_number', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='ИНН ')),
                ('nalog_main', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='ОГРН')),
                ('nalog_registr', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='КПП')),
                ('company_adress', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Адрес юридический')),
                ('number_phone', models.CharField(blank=True, default=None, max_length=13, null=True, verbose_name='Контактный номер телефона')),
                ('mail_adress', models.EmailField(blank=True, default=None, max_length=50, null=True, verbose_name='Адрес эл.почты')),
                ('site_url', models.URLField(blank=True, default=None, null=True, verbose_name='Сайт компании')),
                ('director_name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Директор Ф.И.О')),
                ('bank_name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Наименование банка')),
                ('bank_bik', models.CharField(blank=True, default=None, max_length=9, null=True, verbose_name='БИК банка')),
                ('bank_adress', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Юр.адрес банка')),
                ('bank_invoice', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Расчетный счет')),
                ('bank_edit_invoice', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Кор/счет')),
                ('Comment', models.TextField(blank=True, default=None, max_length=400, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенты ',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Имя контакта')),
                ('number', models.CharField(blank=True, default=None, max_length=14, null=True, verbose_name='Номер телефона')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Телефон клиента',
                'verbose_name_plural': 'Телефоны клиентов',
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
                'verbose_name': 'Статус  ДТП',
                'verbose_name_plural': 'Статусы ДТП',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField(default=False, verbose_name='Клиент ')),
                ('comment', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('accident', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_accident', to='accident.accident', verbose_name='ДТП ')),
                ('car', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_car', to='auto.car', verbose_name='ТС  физ. лица ')),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_client', to='client.client', verbose_name='Физ. лицо  ')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_client', to='client.status', verbose_name='Статус в ДТП  ')),
            ],
            options={
                'verbose_name': 'Участник ДТП',
                'verbose_name_plural': 'Участники ДТП',
            },
        ),
        migrations.CreateModel(
            name='FilePerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Паспорт'), (2, 'Вод.Удост'), (3, 'Реквизиты'), (4, 'Доверенность')], default=None, null=True, verbose_name='Тип')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('scan_doc', models.FileField(default=None, null=True, upload_to='media/person/', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.OneToOneField(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('files_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files_persons', to='client.client', verbose_name='Прикрепленные файлы (Client)')),
            ],
            options={
                'verbose_name': 'Файл Физ.лиц',
                'verbose_name_plural': 'Файлы Физ.лиц',
            },
        ),
        migrations.CreateModel(
            name='FileCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Выписка ОГРН'), (2, 'Реквезиты'), (3, 'Доверенность'), (4, 'Карточка контрагента')], default=None, null=True, verbose_name='Тип')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('scan_doc', models.FileField(default=None, null=True, upload_to='media/company/', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.OneToOneField(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('files_comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files_company', to='client.company', verbose_name='Прикрепленные файлы (Company)')),
            ],
            options={
                'verbose_name': 'Файл Юр.лиц',
                'verbose_name_plural': 'Файлы Юр.лиц',
            },
        ),
    ]
