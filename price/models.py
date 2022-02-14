from django.db import models
from client.models import Company

# Create your models here.


class Price(models.Model):
    """Таблица с  прайсом услуг"""
    name = models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name='Номенклатура')
    price = models.IntegerField(blank=True, default=None, verbose_name='Цена')
    extra_charge = models.IntegerField(blank=True, default=None, verbose_name='Наценка')
    comment = models.CharField(max_length=2000, blank=True, default=None, verbose_name='Комментарий')
    date = models.DateField(blank=True, null=True, default=None, verbose_name='Дата  актуален ')
    code_name  = models.CharField(max_length=400, blank=True, default=None, verbose_name='Тэг')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Прайс услуг "
        verbose_name_plural = "Прайсы услуг"
        ordering = ['-created']


class Contract(models.Model):
    """Таблица  данных цессий оплат """
    number = models.CharField(max_length=2000, blank=True, default=None, verbose_name='Номер договора')
    date = models.DateField(blank=True, null=True, default=None, verbose_name='Дата заключения ')

    name = models.CharField(max_length=200,blank=True, default=None, verbose_name='Наименование')
    summa = models.IntegerField(blank=True, default=None, verbose_name='Сумма договора')
    contragent = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                related_name='contragent_contract', verbose_name='Контрагент')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                related_name='company_contract', verbose_name='Организация')
    comment  = models.CharField(max_length=7000, blank=True, default=None, verbose_name='Коментарий')
    contract_pdf = models.FileField(upload_to='upload/price/', null=True, default=None, blank=True,
                                    verbose_name="Файл договора")

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Договор  "
        verbose_name_plural = "Договора "
        ordering = ['-created']

class Bank_pay(models.Model):
    """Таблица  данных цессий оплат"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                 related_name='company_pay', verbose_name='Страхователь  ')
    summa = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True, default=0,
                                verbose_name='Сумма Контракта')
    pay_number = models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name='Номер платежки')
    pay_date = models.DateField(blank=True, null=True, default=None, verbose_name='Дата платежа ')
    bank_pay_pdf = models.FileField(upload_to='upload/price/', null=True, default=None, blank=True,
                             verbose_name="Файл платежки")
    comment = models.CharField(max_length=2000, blank=True, null=True, default=None, verbose_name='Комментарий')
    date_create = models.DateField(blank=True, null=True, default=None)
    draft = models.BooleanField("Черновик", default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Платеж по цессии  "
        verbose_name_plural = "Платежи по цессиям "
        ordering = ['-created']

