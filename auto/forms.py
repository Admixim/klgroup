from django.shortcuts import render
from .models import Car, Model, Brend, File

from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, FileInput, ClearableFileInput
from django.forms import formset_factory
from django.forms import modelformset_factory
from django import forms


class AutoForm(ModelForm):
    class Meta:
        model = Car
        fields = ["id",
                  "number",
                  "model",
                  "marka",
                  "sts_s",
                  "color",
                  "date_made",
                  "sts_n",
                  "sts_date",
                  "pts_n",
                  "pts_s",
                  "pts_date",
                  "vin",
                  "insurance_number",
                  "insurance_date",
                  # "insurance_company",
                  "insurance_doc",
                  "insurance_numberk",
                  "insurance_datek",
                  # "insurance_companyk",
                  "insurance_dock",
                ]

        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер ТС'
            }),
            "marka": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Марка'
            }),
            "model": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Модель'
            }),
            "color": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цвет ТС'
            }),
            "date_made": DateInput(format='%Y', attrs={
                'data-date-format': 'yyyy',
                'class': 'form-control',
                'placeholder': 'Дата выпуска',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',

            }),
            "sts_n": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер СТС'
            }),
            "sts_s": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия СТС'
            }),
            "sts_date": DateInput(format='%d/%m/%Y', attrs={
                'data-date-format': 'dd/mm/yyyy',
                'class': 'form-control',
                'placeholder': 'Дата выдачи СТС',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
            }),
            "pts_n": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер ПТС'
            }),
            "pts_s": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия ПТС'
            }),
            "pts_date": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи ПТС',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
            }),

            "vin": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'VIN/Кузов Номер'
            }),
            "insurance_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '№ Страх.Пол.'
            }),
            "insurance_date": DateInput(format='%d/%m/%Y', attrs={
                'data-date-format': 'dd/mm/yyyy',
                'class': 'form-control',
                'placeholder': 'Дата  выдачи СтрахПол.',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
            }),
            # "insurance_company": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Страховая Компания'
            # }),
            "insurance_doc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Скан-файл СтрахПолиса'
            }),
            "insurance_numberk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': '№ Страх.Пол.КАСКО'
            }),
            "insurance_datek": DateInput(format='%d/%m/%Y', attrs={
                'data-date-format': 'dd/mm/yyyy',
                'class': 'form-control',
                'placeholder': 'Дата  выдачи СтрахПол. КАСКО',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',

            }),
            # "insurance_companyk": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Страховая Компания КАСКО'
            # }),
            "insurance_dock": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Скан-файл СтрахПолисаКАСКО'
            }),

        }


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ["id",
                  "files",
                  "types",
                  "description",
                  "scan_doc",

                  ]

        widgets = {

            "files": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Страховая Компания КАСКО'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Комментарий',

            }),
            "scan_doc": FileInput(attrs={
                'class': 'form-control'}),
        }


# FileFormset = formset_factory(FileForm, extra=2)


FileFormset = modelformset_factory(
    File,
    fields=('files', 'types', 'description', 'scan_doc'),
    extra=1,
    widgets={
        'files': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Author Name here'
            }
        ),
        'types': forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Тип файла'
            }
        ),
        'description': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Описание к файлу'
            }
        ),
        'scan_doc': forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Файл'
            }
        ),
    }
)
