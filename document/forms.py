from django.shortcuts import render
from  .models import Car,Model,Brend

from django.forms import ModelForm,TextInput,Textarea,DateInput


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
                  "insurance_company",
                  "insurance_doc",
                  "insurance_numberk",
                  "insurance_datek",
                  "insurance_companyk",
                  "insurance_dock",
                  "Comment"
                  ]

        widgets = {
            "number":TextInput(attrs={
            'class':'form-control',
                'placeholder':'Номер ТС'
            }),
            "marka": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель'
            }),
            "color": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цвет ТС'
            }),
            "date_made": DateInput(attrs={
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
            "sts_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи СТС',
                'data-date-container':'#datepicker2',
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
            "pts_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи ПТС',
                'data-date-container':'#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
            }),
            "vin": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'VIN/Кузов Номер'
            }),
            "insurance_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '№ Страх.Пол.'
            }),
            "insurance_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата  выдачи СтрахПол.',
                'data-date-container':'#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
            }),
            "insurance_company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страховая Компания'
            }),
            "insurance_doc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Скан-файл СтрахПолиса'
            }),
            "insurance_numberk": Textarea(attrs={
                'class': 'form-control',
                'placeholder': '№ Страх.Пол.КАСКО'
            }),
            "insurance_datek": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата  выдачи СтрахПол. КАСКО',
                'data-date-container':'#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',

            }),
            "insurance_companyk": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страховая Компания КАСКО'
            }),
            "insurance_dock": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Скан-файл СтрахПолисаКАСКО'
            }),
            "Comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',

            }),

        }


