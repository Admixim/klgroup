from django.db import models



class Status(models.Model):
    """Таблица статусов  судебный операций"""

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
        verbose_name = 'Статус  судебной оперции'
        verbose_name_plural = 'Статусы судебных операций'



class worker(models.Model):
    """Список  сотрудников юристы"""

    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Имя ')
    surname = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Фамилия ')
    midlename = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None,
        verbose_name='Отчество ')
    phone = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер телефона')
    post_mail = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес Эл.почты')
    work_mail = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес Эл.почты рабочей')
    link_social = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес в соц.сети')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' {} {}'.format(self.name, self.surname )

    class Meta:
        verbose_name = "Сотрудник "
        verbose_name_plural = "Сотрудники "
        ordering = ['-created']


class judge_help(models.Model):
        """Список помошников судей """

        name = models.CharField(
            max_length=100,
            blank=True,
            null=True,
            default=None,
            verbose_name='Помошник судьи  ФИО')
        message = models.CharField(
            max_length=500,
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
            verbose_name = "Помошник судьи "
            verbose_name_plural = "Помошники судей"
            ordering = ['-created']


class judge(models.Model):
    """Список судей """

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Судья Ф.И.О. ')
    adress_mail = models.EmailField(
        max_length=300,
        blank=True,
        null=True,
        default=None,
        verbose_name='Электронный адрес ')
    contact_phone = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        default=None,
        verbose_name='Контактный телефон ')
    judge_help = models.ForeignKey(
        judge_help,
        on_delete=models.CASCADE,
        related_name='judge_help',
        blank=True,
        null=True,
        default=None,
        verbose_name='Секретарь судьи ')
    message = models.CharField(
        max_length=500,
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
        verbose_name = "Судья Ф.И.О "
        verbose_name_plural = "Судьи Ф.И.О"
        ordering = ['-created']


class ListCourt(models.Model):
    """Таблица основных  данных о судебных процессе """

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Наименование суда ')
    adress = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        default=None,
        verbose_name='Адрес Суда ')
    adress_post = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        default=None,
        verbose_name='Почтовый адрес ')
    adress_mail = models.EmailField(
        max_length=300,
        blank=True,
        null=True,
        default=None,
        verbose_name='Электронный адрес ')
    contact_phone = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        default=None,
        verbose_name='Контактный телефон ')
    judge = models.ForeignKey(
        judge,
        on_delete=models.CASCADE,
        related_name='judge',
        blank=True, default=None,
        verbose_name='Судья Ф.И.О. ')
    judge_help = models.ForeignKey(
        judge_help,
        on_delete=models.CASCADE,
        related_name='judge_help1',
        blank=True,
        null=True,
        default=None,
        verbose_name='Секретарь судьи ')
    message = models.CharField(
        max_length=2000,
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
        verbose_name = "Справочник судебных участков "
        verbose_name_plural = "Справочник судебных участков"
        ordering = ['-created']


class InfoCourt(models.Model):
    """Информация о деле"""



    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name='Статус  дела',
        related_name='court_status',
        default=None,
        blank=True,
        null=True
                               )
    judge = models.ForeignKey(
        judge,
        on_delete=models.CASCADE,
        verbose_name='Судья',
        related_name='court_judge',
        default=None,
        blank=True,
        null=True
                               )

    case_number = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер Судебного дела')
    uid_number = models.CharField(
        max_length=26,
        blank=True,
        null=True,
        default=None,
        verbose_name='УИД Судебного дела')
    data_reg = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Дата регистрации дела')
    location = models.ForeignKey(
        ListCourt,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='location', verbose_name='Место  ')
    message = models.TextField(
        max_length=50000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Результат события Коментарий')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s"  % self.uid_number

    class Meta:
        verbose_name = "Информация дела"
        verbose_name_plural = "Информация дела"
        ordering = ['-created']

    def get_list(self):
        return self.location.name


class Procedure(models.Model):
    """Таблица операций   судебного процесса """

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Имя операции ')
    message = models.CharField(
        max_length=500,
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
        verbose_name = "Событие "
        verbose_name_plural = "События"
        ordering = ['-created']


class ListEnd(models.Model):
    """Список наменований утверждений для окончания сроков, вступления в силу документов"""

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None,
        verbose_name='Событие утверждения')
    message = models.CharField(
        max_length=500,
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
        verbose_name = "Список окончания сроков вступления в силу "
        verbose_name_plural = "Списки окончания сроков вступления в силу"
        ordering = ['-created']


class Court(models.Model):
    """Таблица основных  данных о судебных процессе """


    info_court = models.ForeignKey(
        InfoCourt,
        on_delete=models.CASCADE,
        related_name='info_court',
        blank=True,
        null=True,
        default=None,
        verbose_name='Список юр.оперций '
            )

    serves_hot_dogs = models.BooleanField(
        default=False,
        verbose_name='Исполнен')
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name='procedure',
        verbose_name='Наименование события')
    worker = models.ForeignKey(
        worker,
        on_delete=models.CASCADE,
        related_name='worker',
        verbose_name='Отв-ный')
    data_finish = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Срок исполнения С')
    date_start = models.DateTimeField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Начало исполнения С')
    date_stop = models.DateTimeField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Завершения исполнения С')
    akt_end = models.ForeignKey(
        ListEnd,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='akt_end',
        verbose_name='Событие утверждения')
    time_stop = models.DateField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Время завершение операции ')
    file_paste = models.FileField(
        upload_to='upload/Courtdoc/',
        null=True,
        blank=True,
        default=None,
        verbose_name='"Файл прикрепленный')
    curt_hall = models.CharField(
        max_length=24,
        blank=True,
        null=True,
        default=None,
        verbose_name='Номер кабинета заседания')
    message = models.TextField(
        max_length=50000,
        blank=True,
        null=True,
        default=None,
        verbose_name='Результат,коментарий события ')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.procedure

    class Meta:
        verbose_name = "Оперция судопроизводства"
        verbose_name_plural = "Оперции судопроизводства"
        ordering = ['-created']

