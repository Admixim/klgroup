# coding: utf-8
from django.db import models
from client.models import Company


class Table(models.Model):
    """Таблица имени модели"""

    name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Таблица ')
    comment = models.CharField(
        max_length=3000,
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
        verbose_name = 'Модель БД '
        verbose_name_plural = 'Модели БД'


class Document(models.Model):
    """Таблица Документов"""

    name = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        default=None,
        verbose_name='Название документа ')

    executor = models.ForeignKey(
        Company,
        max_length=30,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        verbose_name='Исполнитель')

    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Местоположение ')
    author = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Автор документа')
    customer = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Заказчик ')
    comment = models.CharField(
        max_length=3000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий ')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Body_doc(models.Model):
    """Таблица полей документа"""

    name = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        default=None,
        verbose_name='Название объекта  док')
    text = models.TextField(
        max_length=10000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Поле объекта док ')
    document = models.ForeignKey(
        Document,
        max_length=30,
        on_delete=models.CASCADE,
        verbose_name='Документ')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "поле документа"
        verbose_name_plural = "поля документа"


class Document_tags(models.Model):
    """Таблица ТЭГов в документе"""

    table = models.ForeignKey(
        Table,
        default=None,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Модель')
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Наименование ')
    tags = models.TextField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Тэг')
    model = models.TextField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Поле модели')
    comment = models.CharField(
        max_length=3000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Комментарий ')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Список тэгов в шаблоне"
        verbose_name_plural = "Список тэгов в шаблоне"



