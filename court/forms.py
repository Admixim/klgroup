# coding: utf-8
from django.db.models import QuerySet
from django.forms import ModelForm, TextInput, Textarea, DateInput, DateTimeInput, URLField, EmailField, Select, \
    FileInput, CheckboxInput, modelformset_factory

from accident.models import Accident
from .models import *


class CourtInfoForm(ModelForm):
    """Форма справочной информации о судебном деле"""

    class Meta:
        model = InfoCourt
        fields = [
            "case_number",
            "uid_number",
            "data_reg",
            "location",
            "status",
            "message",
            ("judge"),
        ]

        widgets = {

            "case_number": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Номер  дела'

            }),
            "uid_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'УИД дела'
            }),
            "data_reg": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата  регистрации в суде',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',

            }),
            "location": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Судебная инстанция'

            }),
            "judge": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Судья '

            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус дела'

            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Комментарий к делу  '

            }),
        }


class CourtInfoAddForm(ModelForm):
    """Форма справочной информации о судебном деле"""

    class Meta:
        model = InfoCourt
        fields = [
            "case_number",
            "uid_number",
            "data_reg",
            "location",
            "status",
            "message",
            ("judge"),

        ]

        widgets = {

            "case_number": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'readonly': 'True',
                'placeholder': 'Номер  дела'

            }),
            "uid_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'УИД дела',
                'readonly': 'True',

            }),
            "data_reg": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата  регистрации в суде',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
                'readonly': 'True',
                'disabled': 'disabled',

            }),
            "location": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Судебная инстанция',
                'readonly': 'True',
                'disabled': 'disabled',

            }),
            "judge": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Судья ',
                'readonly': 'True',
                'disabled': 'disabled',

            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус дела',
                'readonly': 'True',
                'disabled': 'disabled',

            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Комментарий к делу  '

            }),
        }


class CourtForm(ModelForm):
    """Форма оперций связанных с  судебным процессом """

    class Meta:
        model = Court

        fields =["date_start",
                 "message",
                 "file_paste",
                 "date_start",
                 "data_finish",
                 "procedure",
                 "akt_end",
                 "worker",
                 "curt_hall",
                 ]

        widgets = {

            "message": Textarea(attrs={
                'class': 'form-control',
                'name': "area",
                'id': "elm1",
                'placeholder': 'Результат,коментарий события '
                            }),
            "file_paste": FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Прикрепить документ',

                }),

            "date_start": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата  начало исполения',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
                           }),

            "data_finish": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Срок исполнения',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',

            }),
            "procedure": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Процедура '

            }),
            "akt_end": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Утверждение '

            }),
            "worker": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Отв-ный'

            }),
            "curt_hall": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Кабинет заседания '

            }),
        }


# CourtFormSet = modelformset_factory(
#     Court,
#     fields=("procedure",
#             "worker",
#             "date_start",
#             "data_finish",
#             "akt_end",
#             "message",
#             "file_paste",
#             "curt_hall",),
#     extra=1,
#     widgets={
#
#         "message": Textarea(attrs={
#             'class': 'form-control',
#             'name': "area",
#
#             'placeholder': 'Результат,коментарий события '
#
#         }),
#         "file_paste": FileInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Прикрепить документ',
#
#             }),
#
#         "date_start": DateInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Начало исполнения ',
#
#             'data-date-format': 'dd/mm/yyyy',
#         }),
#
#         "data_finish": DateInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Срок исполнения ',
#
#             'data-date-format': 'dd/mm/yyyy',
#         }),
#         "procedure": Select(attrs={
#             'class': 'form-control',
#             'placeholder': 'Процедура '
#
#         }),
#         "akt_end": Select(attrs={
#             'class': 'form-control',
#             'placeholder': 'Утверждение '
#
#         }),
#         "worker": Select(attrs={
#             'class': 'form-control',
#             'placeholder': 'Отв-ный'
#
#         })
#     })