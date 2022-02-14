from django.shortcuts import render
from .models import *
from django.forms import ModelForm, TextInput,NumberInput, Textarea, DateInput, Select, FileInput


class ExpertForm(ModelForm):
    class Meta:
        model = Expert
        fields = ["id",
                  "accident",
                  "num_doc",
                  "type",
                  "data_in",
                  "data_out",
                  "summa_exp",
                  "price_nwear",
                  "price_wwear",
                  "price_mmarket",
                  "price_uleftovers",
                  "price_uts",
                  "price_summa",
                  "comment",
                  "contragent",
                  "file_invoce",
                  "file_expert",
                  "client",
                  "car"
                  ]

        widgets = {

            "accident": Select(attrs={
                'align': "left",
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
            'placeholder': 'ДТП'

            }),
            "client": Select(attrs={
                'align': "left",
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
                'placeholder': 'Заказчик экспертизы'
            }),
            "car": Select(attrs={
                'align': "left",
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
                'placeholder': 'ТС заказчика'
            }),

            "type": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Виды оценок'
                }),
            "num_doc": TextInput(attrs={
                'class': 'form-control',
                'align': "left",
                'placeholder': 'Номер экспертизы'
            }),
            "data_in": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата отправления эксперту',
                 'data-date-container':'#datepicker2',
                 'data-provide': 'datepicker',
                 'data-date-autoclose': 'true',
            }),
            "data_out": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата завершение ЭО',
                'data-date-container':'#datepicker2',
                'data-provide': 'datepicker',
                'data - date - autoclose': 'true',

            }),
            "price_nwear": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ВР без износа'
            }),
            "price_wwear": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ВР с износом'
            }),

            "price_mmarket": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Средняя по рынку'
            }),
            "price_uleftovers": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Годные остатки'
            }),
            "price_uts": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма УТС'
            }),
            "price_summa": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма ущерба',

            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'name': "area",
                'id': "elm1",
                'placeholder': 'Коментарий'
            }),
            "contragent": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Контрагент'
            }),
            "summa_exp": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость экспертизы'

            }),
            "file_expert": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл Экспертизы',
            }),
            "file_invoce": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл Чека',
                'type': "file",
            })


        }


class ExpertNewForm(ModelForm):
    class Meta:
        model = Expert
        fields = ["id",
                  "num_doc",
                  "type",
                  "data_in",
                  "data_out",
                  "summa_exp",
                  "price_nwear",
                  "price_wwear",
                  "price_mmarket",
                  "price_uleftovers",
                  "price_uts",
                  "price_summa",
                  "comment",
                  "contragent",
                  "file_invoce",
                  "file_expert",
                  "client",
                  "car"
                  ]

        widgets = {
            "client": Select(attrs={
                'align': "left",
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
                'placeholder': 'Заказчик экспертизы'
            }),
            "car": Select(attrs={
                'align': "left",
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
                'placeholder': 'ТС заказчика'
            }),

            "type": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Виды оценок'
                }),
            "num_doc": TextInput(attrs={
                'class': 'form-control',
                'align': "left",
                'placeholder': 'Номер экспертизы'
            }),
            "data_in": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата отправления эксперту',
                 'data-date-container':'#datepicker2',
                 'data-provide': 'datepicker',
                 'data-date-autoclose': 'true',
            }),
            "data_out": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата завершение ЭО',
                'data-date-container':'#datepicker2',
                'data-provide': 'datepicker',
                'data - date - autoclose': 'true',

            }),
            "price_nwear": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ВР без износа'
            }),
            "price_wwear": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ВР с износом'
            }),

            "price_mmarket": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Средняя по рынку'
            }),
            "price_uleftovers": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Годные остатки'
            }),
            "price_uts": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма УТС'
            }),
            "price_summa": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма ущерба',

            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'name': "area",
                'id': "elm1",
                'placeholder': 'Коментарий'
            }),
            "contragent": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Контрагент'
            }),
            "summa_exp": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость экспертизы'

            }),
            "file_expert": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл Экспертизы',
            }),
            "file_invoce": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл Чека',
                'type': "file",
            })


        }
