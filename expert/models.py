from django.contrib.auth.models import User
from django.db import models
from client.models import Company,Client
from accident.models import Accident
from auto.models import Car

class Type(models.Model):
    """Таблица видов экспертизы"""

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Вид')
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
        verbose_name = 'Вид экспертизы'
        verbose_name_plural = 'Виды экспертизы'


class ExpertComp(models.Model):
    """Таблица организаций и  компаний """

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Наименование')
    comment = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        default=None,
        verbose_name='Описание')
    mail_post = models.EmailField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес Эл.почты')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Экспертная орг. "
        verbose_name_plural = "Экспертные орг."
        ordering = ['-created']



class Expert(models.Model):
    """Таблица данных экспертизы о клиенте """
    accident = models.ForeignKey(
        Accident,
        on_delete=models.CASCADE,
        verbose_name='Экспретиза',
        related_name='expert_accident',
        default=None,
        blank=True,
        null=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Заказчик экспертизы',
        related_name='expert_client',
        default=None,
        blank=True,
        null=True)
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name='Вид экспертизы',
        related_name='expert_type',
        default=None,
        blank=True,
        null=True)

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='ТС Заказчика',
        related_name='expert_car',
        default=None,
        blank=True,
        null=True)
    num_doc = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер экспертизы')
    data_in = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата отправления эксперту')
    data_out = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата ответа эксперта')
    price_nwear =models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='ВР без износа')
    price_wwear =models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='ВР с износом')
    price_mmarket=models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Средняя по рынку')
    price_uleftovers = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Годные остатки')
    price_uts = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Сумма УТС')
    price_summa = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Сумма ущерба')
    comment = models.TextField(
        max_length=100000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Коментарий')
    summa_exp = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Стоимость экспертизы')
    contragent = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='contragent',
        verbose_name='Контрагент')

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # return "%s" % self.contragent
        return 'Компания: {}, Дата : {}, ВР без износа: {}'.format(self.contragent, self.data_out, self.price_nwear)

    class Meta:
        verbose_name = "Экспертиза  "
        verbose_name_plural = "Экспертные оценки"
        ordering = ['-created']

    def get_expert_client(self):
        return self.accident.partner_accident.filter(type=True).first()

    def get_client_type(self) -> str:
        if self.is_type:
            return "Клиент"
        return "Не клиент"

class ExpertFiles(models.Model):
    """Таблица прикрепленных файлов Экспертизы """

    TYPES = (
        (1, 'Акт Осмотра'),
        (2, 'Экспертиза'),
        (3, 'Калькуляция'),
        (3, 'Скан чека'),
    )
    types = models.PositiveSmallIntegerField(
                                            choices=TYPES,
                                            null=True,
                                            default=None,
                                            blank=True,
                                        )

    files = models.ForeignKey(
                                Expert,
                                on_delete=models.CASCADE,
                                related_name='files_expert',
                                blank=True,
                                null=True,
                                verbose_name='Прикрепленные файлы (Expert)'
                            )
    types = models.PositiveSmallIntegerField(choices=TYPES, null=True,
                                             default=None,
                                             blank=True, )
    description = models.CharField(
                                    max_length=100,
                                    verbose_name='Описание '
                                )
    scan_doc = models.FileField(
                                upload_to='media/doc_expert/',
                                null=True,
                                default=None,
                                verbose_name="Файл "
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

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Файл Экспертизы'
        verbose_name_plural = 'Файлы Экспертизы'
