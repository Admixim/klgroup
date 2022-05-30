import uuid

from django.db import models
from court.models import *

# from crm_kl import *


# class client_pay (models.Model):
from django.http import HttpResponse

"""Оплата цессий компаниями"""
#     name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Помошник судьи  ФИО')
#     message = models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name='Комментарий')
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Status(models.Model):
    """Таблица статусов дела ДТП"""

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
        verbose_name = 'Статус  дела о ДТП'
        verbose_name_plural = 'Статусы дела о ДТП'





class AccidentPos(models.Model):
    """Таблица Документ постановление ДТП"""

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Тип документа')
    full_name = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        default=None,
        verbose_name='Полное наименование')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Док опеределение ДТП'
        verbose_name_plural = 'Док определение ДТП'


class AccidentDoc(models.Model):
    """Таблица Документ основние  ДТП"""

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Тип документа')
    full_name = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        default=None,
        verbose_name='Полное наименование')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Док основание  ДТП'
        verbose_name_plural = 'Док основание  ДТП'


class Accident(models.Model):
    """Таблица основных  данных о ДТП """

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name='status_acc',
        blank=True,
        null=True, verbose_name='Статус  дела о ДТП')
    data = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата ДТП ')
    time = models.TimeField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Время ДТП ')
    location_accident = models.CharField(
        max_length=400,
        blank=True,
        default=None,
        verbose_name='Место ДТП')
    number = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер протокола')
    dtp_doc = models.ForeignKey(
        AccidentDoc,
        on_delete=models.CASCADE,
        related_name='dtp_doc',
        blank=True,
        null=True, verbose_name='Документ Основание ')

    file_doc = models.FileField(
        upload_to='upload/protokol_doc/',
        null=True, default=None,
        verbose_name="Файл Основание",
        blank=True, )

    dtp_pos = models.ForeignKey(
        AccidentPos,
        on_delete=models.CASCADE,
        related_name='AccidentPos',
        blank=True,
        null=True,
        verbose_name='Документ Постановление ')
    file_pos = models.FileField(
        upload_to='upload/protokol_pos/',
        null=True,
        default=None,
        blank=True,
        verbose_name="Файл Постановление")

# Данные по судебному делу

    court_info = models.ForeignKey(
        InfoCourt,
        on_delete=models.CASCADE,
        related_name='court_info',
        blank=True,
        null=True, verbose_name='Инфо о Судопроизводстве')

    data_insurance = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата обращения в Страховую')

    message = models.CharField(
        max_length=100000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий')
    slug = models.SlugField(max_length=200, default=uuid.uuid1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # return "%s" % self.id
        return 'id {}, номер {}, место дтп {}, клиент{}'.format(self.id, self.number, self.location_accident,
                                    self.partner_accident.filter(type='True').first())

    class Meta:
        verbose_name = "ДТП  "
        verbose_name_plural = "ДТП"
        ordering = ['-created']
    # Сохранение файлов  в  модлеи джанго

    # def save(self, *args, **kwargs):
    #     if self.file_doc:
    #         # save file for get path
    #         new_path = self.file_doc.name.split(".").pop(1)
    #         self.file_doc.name = "my_name"+new_path
    #     super().save(*args, **kwargs)

    def get_accident(self):
        b = self.partner_accident.filter(type='True').first()

        return HttpResponse(f'{b.car.model}')
    def get_acciden(self):
        info = Accident.court_info.pk
        name = self.name + self.surname
        return info, name