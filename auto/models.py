from django.db import models
from django.contrib.auth.models import User
# from client.models import Company


class Brend(models.Model):
    """Список марок ТС"""

    name = models.CharField(
                            max_length=30,
                            blank=True,
                            null=True,
                            default=None,
                            verbose_name='Марка ТС '
                            )
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
                                    verbose_name='Марка Авто',
                                    related_name='brand_model'
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
                            verbose_name='Цвет'
                        )
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
                                verbose_name='Номер СТС'
                            )
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
                            verbose_name='VIN номер'
                        )

    driver = models.CharField(
                                max_length=24,
                                blank=True,
                                null=True,
                                default=None,
                                verbose_name='Сделать ссылку на клиента '
                            )

    Comment = models.CharField(
                                max_length=500,
                                blank=True, null=True,
                                default=None,
                                verbose_name='Комментарий'
                            )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(
                                    auto_now_add=True,
                                    auto_now=False
                                )
    updated = models.DateTimeField(
                                    auto_now_add=False,
                                    auto_now=True
                                )

    def __str__(self):
        return '{} {} {}'.format(self.number, self.model, self.marka)

    def get_model(self):
        return '{} {}'.format(self.model.pk, self.model.name)

    class Meta:
        verbose_name = "Транспортное средство  "
        verbose_name_plural = "Транспортные средства"
        ordering = ['-created']


class Insurance(models.Model):
    """Таблица данных страховых полисов ТС"""
    car = models.ForeignKey(
                            Car,
                            on_delete=models.CASCADE,
                            related_name='insurance_auto',

                            verbose_name=' Полисы страхования ТС'
                        )
    TYPES = (
        (1, 'ОСАГО'),
        (2, 'Каско'),
        (3, 'Доп.соглашение'),
    )
    types = models.PositiveSmallIntegerField(choices=TYPES, null=True,

                                             blank=True,
                                             )
    i_serial = models.CharField(max_length=10,
                                verbose_name='Серия '
                                )
    i_number = models.CharField(max_length=15,
                                verbose_name='Номер'
                                )
    start_date = models.DateField(
                                    blank=True,
                                    null=True,
                                    default=None,
                                    verbose_name='Дата выдачи'
                                    )
    end_date = models.DateField(
                                blank=True,
                                null=True,
                                default=None,
                                verbose_name='Дата окончания'
                                )

    description = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name='Описание'
                                   )
    author = models.OneToOneField(
                                    User,
                                    db_column='user',
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,
                                )
    created = models.DateTimeField(
                                    auto_now_add=True,
                                    auto_now=False
                                )
    updated = models.DateTimeField(
                                    auto_now_add=False,
                                    auto_now=True
                                )

    class Meta:
        verbose_name = 'Страховой документ ТС'
        verbose_name_plural = 'Страховые  документы ТС'


class AutoFiles(models.Model):
    """Таблица прикрепленных файлов ТС """

    TYPES = (
        (1, 'ПТС'),
        (2, 'СТС'),
        (3, 'Договор КП'),
        (4, 'ОСАГО'),
        (5, 'КАСКО'),
    )
    types = models.PositiveSmallIntegerField(
                                            choices=TYPES,
                                            null=True,
                                            default=None,
                                            blank=True,
                                        )

    files = models.ForeignKey(
                                Car,
                                on_delete=models.CASCADE,
                                related_name='files_auto',
                                blank=True,
                                null=True,
                                verbose_name='Прикрепленные файлы (Car)'
                            )
    types = models.PositiveSmallIntegerField(choices=TYPES, null=True,
                                             default=None,
                                             blank=True, )
    description = models.CharField(
                                    max_length=100,
                                    verbose_name='Описание'
                                )
    scan_doc = models.FileField(
                                upload_to='media/auto/',
                                null=True,
                                default=None,
                                verbose_name="Файл"
                            )
    author = models.OneToOneField(
                                    User,
                                    db_column='user',
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,
                                )
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Файл ТС'
        verbose_name_plural = 'Файлы ТС'
