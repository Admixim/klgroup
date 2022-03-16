from django.db import models
# from client.models import Company


class Brend(models.Model):
    """Список марок ТС"""

    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Марка ТС ')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка ТС"
        verbose_name_plural = "Марки ТС"


class Model(models.Model):
    """Список моделей ТС"""

    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Модель ТС '
    )
    brand_auto = models.ForeignKey(
        Brend,
        on_delete=models.CASCADE,
        verbose_name='Марка Авто'
    )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'automarket_target_model'

    ordering = ['brand_auto', 'name']
    verbose_name = "Модель ТС"
    verbose_name_plural = "Модель ТС"


class Car(models.Model):
    """Таблица основных  данных ТС """

    model = models.ForeignKey(
        Model, blank=True,
        on_delete=models.CASCADE,
        related_name='model',
        null=True,
        verbose_name='Модель '
    )
    marka = models.ForeignKey(
        Brend,
        blank=True,
        on_delete=models.CASCADE,
        related_name='marka',
        null=True,
        verbose_name='Марка '
    )
    number = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Гос.номер '
    )
    color = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Цвет')
    date_made = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name='Год выпуска'
    )
    sts_s = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        default=None,
        verbose_name='Серия СТС'
    )
    sts_n = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер СТС')
    sts_date = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата выдачи СТС'
    )
    pts_s = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        default=None,
        verbose_name='Серия ПТС'
    )
    pts_n = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер ПТС'
    )
    pts_date = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата выдачи ПТС'
    )
    vin = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='VIN номер')
    insurance_number = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер полиса страхования ОСАГО'
    )
    insurance_date = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата выдачи полиса ОСАГО'
    )
    # insurance_company = models.ForeignKey(
    #     Company,
    #     blank=True,
    #     on_delete=models.CASCADE,
    #     related_name='insurance_company',
    #     null=True,
    #     verbose_name='Страховая компания ОСАГО'
    # )
    insurance_doc = models.FileField(
        upload_to='upload/auto/insurance_osago/',
        null=True, default=None,
        blank=True,
        verbose_name="Скан полиса ОСАГО"
    )
    insurance_numberk = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер полиса страхования КАСКО'
    )
    insurance_datek = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата выдачи полиса КАСКО'
    )
    # insurance_companyk = models.ForeignKey(
    #     Company,
    #     on_delete=models.CASCADE,
    #     related_name='insurance_companyk',
    #     null=True, blank=True,
    #     verbose_name='Страховая компания КАСКО'
    # )
    insurance_dock = models.FileField(
        upload_to='upload/auto/insurance_kasko/',
        null=True, default=None,
        blank=True,
        verbose_name="Скан полиса КАСКО"
    )
    driver = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Сделать ссылку на клиента ')
    doc_pass = models.FileField(
        upload_to='upload/client/pasport/',
        null=True,
        default=None,
        blank=True,
        verbose_name="Фото ПТС"
    )
    Comment = models.CharField(
        max_length=500,
        blank=True, null=True,
        default=None,
        verbose_name='Комментарий'
    )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.number, self.model, self.marka)

    class Meta:
        verbose_name = "Транспортное средство  "
        verbose_name_plural = "Транспортные средства"
        ordering = ['-created']


class File(models.Model):
    """Таблица прикрепить файлы документов """
    TYPES = (
        (1, 'ПТС'),
        (2, 'СТС'),
        (3, 'Договор КП'),
        (4, ''),
    )
    files = models.ForeignKey(
        Car,
        blank=True,
        on_delete=models.CASCADE,
        related_name='files1',
        null=True,
        verbose_name='Прикрепленные файлы (Car)'
    )
    types = models.PositiveSmallIntegerField(choices=TYPES,)
    description = models.CharField(max_length=100, verbose_name='Описание')
    scan_doc = models.FileField(
        upload_to='media/auto/',
        null=True,
        default=None,
        blank=True,
        verbose_name="Файл"
    )
