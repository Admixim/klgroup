from django.shortcuts import render
from .models import Car, Model, Brend, AutoFiles, Insurance
from django.forms import modelformset_factory
from django.forms import (
    NumberInput,
    ModelForm,
    TextInput,
    Textarea,
    DateInput,
    Select,
    EmailInput,
    URLInput,
    FileInput,
)


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
                'id': 'model-select',
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
        }


class FileForm(ModelForm):
    class Meta:
        model = AutoFiles
        fields = ["id",
                  "files",
                  "types",
                  "description",
                  "scan_doc",
                  ]

        widgets = {

            "files": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Файл ТС'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Описание',

            }),
            "scan_doc": FileInput(attrs={
                'class': 'form-control'}),
            'placeholder': 'Файл',
        }


InsuranceAutoFormset = modelformset_factory(
    Insurance,
    fields=('types',
            'i_serial',
            'i_number',
            'start_date',
            'end_date',
            'description',
            ),
    extra=1,
    widgets={
        'i_serial': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Серия'
            }
        ),
        'types': Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Тип страховки'
            }
        ),
        'description': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Описание к полису'
            }
        ),
        'i_number': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер',
            }
        ),
        'start_date': DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала ',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
            }),
        'end_date': DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата завершения',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
            }),
    }
)


FileAutoFormset = modelformset_factory(
    AutoFiles,
    fields=('files',
            'types',
            'description',
            'scan_doc'
            ),
    extra=1,
    widgets={
        'files': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Файлы ТС'
            }
        ),
        'types': Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Тип файла'
            }
        ),
        'description': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Описание к файлу'
            }
        ),
        'scan_doc': FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Файл',
            }
        ),
    }
)
