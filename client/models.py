from django.contrib.auth.models import User
from django.db import models
from accident.models import *
from auto.models import Car
from client.models import *


class Status(models.Model):
    """Таблица статусов участников ДТП"""

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Наименование')
    comment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий')

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус  ДТП'
        verbose_name_plural = 'Статусы ДТП'


class StatusCompany(models.Model):
    """Таблица статусов Контрагента"""

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Наименование')
    comment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий')

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус  контрагента'
        verbose_name_plural = 'Статусы контрагента'

class Phone(models.Model):
    """Таблица телефонов клиентов"""

    name = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Имя контакта')
    number = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер телефона')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.number

    class Meta:
        verbose_name = 'Телефон клиента'
        verbose_name_plural = 'Телефоны клиентов'


class Client(models.Model):
    """Таблица основных  данных о физ лицах """

    name = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Имя ')

    surname = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        verbose_name='Фамилия ')

    midlename = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        verbose_name='Отчество ')

    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Номер телефона')
    phone2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Номер телефона 1')

    serial_pass = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name='Серия паспорта',
        help_text="Вводится 4 цифры без пробела")

    number_pass = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Номер паспорта',
        help_text="Вводится 6 цифр без пробела")

    enter_org = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Кем выдан',
        help_text="УВД,ОВД,ЗАГС, МВД")

    data_create = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата выдачи')

    adress_reg = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Место регистрации')

    adress_home = models.CharField(
        max_length=50, blank=True,
        verbose_name='Место жительства')

    date_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения')

    point_birth = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Место рождение')

    doc_pass = models.FileField(
        default=None,
        blank=True,
        upload_to='client/upload/pasport/',
        verbose_name="Фото паспорта")

    serial_lic = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Серия ВУ',
        help_text="Вводится 4 цифры без пробела")

    number_lic = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер ВУ',
        help_text="Вводится 6 цифр без пробела")

    enter_lic = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Кем выдан ГИБДД')

    create_lic = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата  выдачи')

    adress_lic = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Место выдачи ВУ')

    category = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Категории прав',
        help_text="B,C,D,E,BC,DE,A")

    doc_lic = models.FileField(
        upload_to='assets/img/products_images/',
        null=True,
        default=None,
        blank=True,
        verbose_name="Фото ВУ")

    post_mail = models.EmailField(
        max_length=24,
        blank=True,
        null=True,

        verbose_name='Адрес Эл.почты')

    link_social = models.URLField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес в соц.сети')

    attorney = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата  Окончание доверенности')

    doc_attorney = models.FileField(
        upload_to='upload/doc_attorney/',
        null=True,
        default=None,
        blank=True,
        verbose_name="Файл Доверенности")

    doc_requisites = models.FileField(
        upload_to='upload/doc_requisites/',
        null=True,
        default=None,
        blank=True,
        verbose_name="Файл Реквизитов банк")

    draft = models.BooleanField("Черновик", default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.surname, self.midlename)

    class Meta:
        verbose_name = "Клиент  "
        verbose_name_plural = "Клиенты"
        ordering = ['-created']


class Company(models.Model):
    """Таблица Контрагента  """

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
        , default=None,
        verbose_name='Название компании')
    full_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Полное наименование компании')
    StatusCompany = models.ForeignKey(
        StatusCompany,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='status_company',
        verbose_name='Статус контрагента  ')
    nalog_number = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='ИНН ')
    nalog_main = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='ОГРН')
    nalog_registr = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='КПП')
    company_adress = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес юридический')
    number_phone = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        default=None,
        verbose_name='Контактный номер телефона')
    mail_adress = models.EmailField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес эл.почты')
    site_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Сайт компании')

    director_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Директор Ф.И.О')

    bank_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Наименование банка')
    bank_bik = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        default=None,
        verbose_name='БИК банка')
    bank_adress = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Юр.адрес банка')
    bank_invoice = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default=None,
        verbose_name='Расчетный счет')
    bank_edit_invoice = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default=None,
        verbose_name='Кор/счет')
    Comment = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты "
        ordering = ['-created']


class Partner(models.Model):
    """Таблица сторон ДТП"""

    type = models.BooleanField(default=False,
                               verbose_name='Клиент ')

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='status_client',
        verbose_name='Статус в ДТП  ')

    accident = models.ForeignKey(
        Accident,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='partner_accident',
        verbose_name='ДТП ')

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='partner_client',
        verbose_name='Физ. лицо  ')
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='partner_car',
        verbose_name='ТС  физ. лица ')

    comment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий')

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.status

    class Meta:
        verbose_name = 'Участник ДТП'
        verbose_name_plural = 'Участники ДТП'

    def get_fullname(self):
        return self.client

    def get_carfullname(self):
        marka = self.car.marka
        model = self.car.model
        number = self.car.number
        color = self.car.color
        data =number +'/n' + (f'{marka}') + '/n' + (f'{model}') + color
        return data


    def get_client(self):
        return self.accident.partner_accident.filter(type=True).first()

    def get_file_client(self):
        files = Partner.client.files_persons
        for item in files.all():
            print(item)
            return  item


class FileCompany(models.Model):
    """Таблица прикрепить файлы документов Юр лица"""
    TYPES = (
        (1, 'Выписка ОГРН'),
        (2, 'Реквезиты'),
        (3, 'Доверенность'),
        (4, 'Карточка контрагента'),

    )
    files_comp = models.ForeignKey(
        Company,
        blank=True,
        on_delete=models.CASCADE,
        related_name='files_company',
        null=True,
        verbose_name='Прикрепленные файлы (Company)'
    )
    types = models.PositiveSmallIntegerField(choices=TYPES,
                                             verbose_name='Тип',
                                             null=True,
                                             default=None,
                                             blank=True,
                                             )
    description = models.CharField(max_length=100, verbose_name='Описание')
    scan_doc = models.FileField(
        upload_to='media/company/',
        null=True,
        default=None,
        verbose_name="Файл"
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Файл Юр.лиц'
        verbose_name_plural = 'Файлы Юр.лиц'


class FilePerson(models.Model):
    """Таблица прикрепить файлы документов физ лица """
    TYPES = (
        (1, 'Паспорт'),
        (2, 'Вод.Удост'),
        (3, 'Реквизиты'),
        (4, 'Доверенность'),
    )
    files_person = models.ForeignKey(
        Client,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='files_persons',
        verbose_name='Прикрепленные файлы (Client)'
    )
    types = models.PositiveSmallIntegerField(
        choices=TYPES,
        verbose_name='Тип',
        null=True,
        default=None,
        blank=True,
    )
    description = models.CharField(max_length=100, verbose_name='Описание')
    scan_doc = models.FileField(
        upload_to='media/person/',
        null=True,
        default=None,
        verbose_name="Файл"
    )
    author = models.OneToOneField(User, db_column='user', on_delete=models.CASCADE, blank=True, null=True, )
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Файл Физ.лиц'
        verbose_name_plural = 'Файлы Физ.лиц'
