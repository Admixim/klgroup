# coding: utf-8
from django.forms import ModelForm, TextInput, Textarea, DateInput,URLField,EmailField,Select,FileInput
from .models import *

class CourtInfoForm(ModelForm):
    """Форма справочной информации о судебном деле"""
    class Meta:
        model = InfoCourt
        fields =["case_number",
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


class CourtForm(ModelForm):
    """Форма справочной информации о судебном деле"""
    class Meta:
        model = Court
        fields = [
                "procedure",
                "worker",
                "message",
                "file_paste",
                "date_start",
                "data_finish",
                "akt_end",
                ]

        widgets = {
            "message": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Результат,коментарий события '

            }),
            "file_paste": FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Прикрепить документ',

                }),

            "date_start": DateInput(format='%d/%m/%Y', attrs={
                        'class': 'form-control',
                        'placeholder': 'Начало исполнения ',
                        'data-date-container': '#datepicker2',
                        'data-provide': 'datepicker',
                        'data-date-autoclose': 'true',
                        'data-date-format': 'dd/mm/yyyy',

                        }),

            "data_finish": DateInput(format='%d/%m/%Y',attrs={
                        'class': 'form-control',
                        'placeholder': 'Срок исполнения ',
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

            })

        }







