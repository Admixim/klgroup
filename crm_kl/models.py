from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    # Категории в меню с левой стороны CRM


    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



class order_site(models.Model):
    """Форма заявки  на сайте """

    name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Имя Фамилия')
    message = models.CharField(max_length=5000, blank=True, null=True, default=None, verbose_name='Цель обращения')
    contact = models.CharField(max_length=15, blank=True, null=True, default=None, verbose_name='Контактный номер')
    email = models.EmailField(max_length=254,verbose_name='Электронный адрес')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Заявки сайт "
        verbose_name_plural = "Заявки сайт"
        ordering = ['-created']

class question(models.Model):
    """Форма вопрос ответ  на сайте """

    name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Имя Фамилия')
    contact = models.CharField(max_length=15, blank=True, null=True, default=None, verbose_name='Контактный номер')
    email = models.EmailField(max_length=254, verbose_name='Электронный адрес')
    service =  models.CharField(max_length=15, blank=True, null=True, default=None, verbose_name='Интересующая услуга')
    message = models.CharField(max_length=5000, blank=True, null=True, default=None, verbose_name='Цель обращения')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Вопросы сайт "
        verbose_name_plural = "Вопросы сайт"
        ordering = ['-created']




# class responsible(models.Model):
#     """Ответственный  по выдачи средств"""

#     name = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Имя')
#     full_name = models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name='Фамилия')
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# class client_pay(models.Model):
#     """Таблица финансовых операций  """
#
#     # contract = models.ForeignKey(, on_delete=models.CASCADE, related_name='contract', blank=True,
#     #                             null=True,
#     #                             verbose_name='Договор/ПРотокол ДТП')
#     plaintiff = models.ForeignKey(base.plaintiff, on_delete=models.CASCADE, related_name='plaintiff', blank=True,
#                                 null=True,
#                                 verbose_name='Клиент ')
#     car_plaintiff = models.ForeignKey(base.car_plaintiff, on_delete=models.CASCADE, default=None, blank=True,
#                                       related_name='car_plaintiff', verbose_name='Автомобиль истца ')
#     culprit = models.ForeignKey(base.culprit, on_delete=models.CASCADE, blank=True, null=True, related_name='culprit',
#                                 verbose_name='Ответчик ')
#     car_culprit = models.ForeignKey(base.car_culprit, on_delete=models.CASCADE, blank=True, null=True, related_name='car_culprit',
#                                     verbose_name='Автомобиль ответчика ')
#
#     responsible = models.ForeignKey(models.responsible, on_delete=models.CASCADE, blank=True, null=True, related_name='responsible',
#                                 verbose_name='Ответственный')
#
#     PAY_METHOD = (('Наличный'),('безналичный'))
#     pay_method =models.CharField(max_length=1, choices=PAY_METHOD)
#     time = models.TimeField(blank=True, null=True, default=None, verbose_name='Время ДТП ')
#     number = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name='Номер протокола')
#     dtp_doc = models.ForeignKey(AccidentDoc, on_delete=models.CASCADE, related_name='AccidentDoc', blank=True,
#                                 null=True, verbose_name='Документ Основание ')
#     doc_isk = models.BooleanField(verbose_name= ("Исковое заявление"), default=None, help_text=("Исковое заявление"))
#     doc_pos = models.BooleanField(verbose_name=("Пошлина"), default=None, help_text=("Пошлина"))
#     doc_spr = models.BooleanField(verbose_name=("Экспертиза"), default=None, help_text=("Экспертиза"))
#     doc_dtp = models.BooleanField(verbose_name=("Протокол ДТП"), default=None, help_text=("Протокол ДТП"))
#
#
#
#     doc = models.FileField(upload_to='upload/protokol_doc/', null=True, default=None,
#                            verbose_name="Файл Основание", blank=True, )
#     dtp_pos = models.ForeignKey(AccidentPos, on_delete=models.CASCADE, related_name='AccidentPos', blank=True,
#                                 null=True,
#                                 verbose_name='Документ Постановление ')
#     doc_1 = models.FileField(upload_to='upload/protokol_doc/', null=True, default=None, blank=True,
#                              verbose_name="Файл Дополнение")
#     case_number = models.CharField(max_length=24, blank=True, null=True, default=None,
#                                    verbose_name='N дела')
#     uid_number = models.CharField(max_length=26, blank=True, null=True, default=None, verbose_name='UID дела')
#     data_reg = models.DateField(blank=True, null=True, default=None, verbose_name='Дата регистрации дела')
#     location_court = models.ForeignKey(ListCourt, on_delete=models.CASCADE, blank=True, null=True,
#                                        default=None, related_name='location', verbose_name='Судебный участок  ')
#     location_accident = models.CharField(max_length=400, blank=True, default=None, verbose_name='Место ДТП')
#     plaintiff = models.ForeignKey(Client, on_delete=models.CASCADE, default=None, blank=True, related_name='plaintiff',
#                                   verbose_name='Истец ')
#     car_plaintiff = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, blank=True,
#                                       related_name='car_plaintiff', verbose_name='Автомобиль истца ')
#     culprit = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True, related_name='culprit',
#                                 verbose_name='Ответчик ')
#     car_culprit = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True, related_name='car_culprit',
#                                     verbose_name='Автомобиль ответчика ')
#     data_insurance = models.DateField(blank=True, null=True, default=None, verbose_name='Дата обращения в Страховую')
#     message = models.CharField(max_length=1000, blank=True, null=True, default=None, verbose_name='Комментарий')
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#
    # def __str__(self):
    #     # return "%s" % self.id
    #     return '{},{},{}'.format(self.id, self.data,self.car_plaintiff)
    #
    # class Meta:
    #     verbose_name = "Финансовыве операции  "
    #     verbose_name_plural = "Финансовыве операции"
    #     ordering = ['-created']
    # def save(self, *args, **kwargs):
    #     if self.doc_1:
    #         # save file for get path
    #         new_path = self.doc_1.name.split(".").pop(1)
    #         self.doc_1.name = "my_name"+new_path
    #         super().save(*args, **kwargs)
