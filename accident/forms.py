from django.shortcuts import render
from .models import *
from django.forms import ModelForm,\
                        TextInput,\
                        Textarea,\
                        DateInput, \
                        TimeInput, \
                        Select, \
                        FileInput, \
                        SelectDateWidget


class AccidentForm(ModelForm):
    # Форма Создание записи ДТП

    class Meta:
        model = Accident
        fields = [
            "number",
            "location_accident",
            "status",
            "data",
            "time",
            "number",
            "dtp_doc",
            "file_doc",
            "dtp_pos",
            "file_pos",
            "data_insurance",
            "message",
        ]

        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Номер протокола'

            }),
            "location_accident": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Место ДТП'
            }),
            "data": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата  ДТП',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',

            }),

            "time": TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
                'placeholder': 'Время ДТП',
                # 'type': 'time',
                'data-time-format': '%H:%M',
            }),
            "dtp_doc": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Документ Основание'

            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус о дтп ДТП'
        }),



            "dtp_pos": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Документ Постановление'
            }),
            "file_doc": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Прикрепить'
            }),
            "file_pos": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Прикрепить'
            }),


            "human": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Участник ДТП'
            }),
            "car": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автомобиль участника'
            }),
        }



class AccidentAddPartnerForm(ModelForm):
     # Форма Создание записи ДТП


    class Meta:
        model = Accident
        fields = [
            "number",
            "location_accident",
            "data",
            "time",
            "number",
            "dtp_doc",
            "file_doc",
            "dtp_pos",
            "file_pos",
            "data_insurance",
            "message",
        ]

        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'type' : 'text',
                'readonly': 'True',
                'placeholder': 'Номер протокола'

            }),
            "location_accident": Textarea(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'placeholder': 'Место ДТП'
            }),
            "data": DateInput(format='%d/%m/%Y',attrs={
                'class': 'form-control',
                # 'readonly': 'True',
                'placeholder': 'Дата  ДТП',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'disabled': 'disabled',

            }),

            "time": TimeInput(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'type':'time',
                'id': 'example-time-input',
                'placeholder': 'Время ДТП'
            }),
            "dtp_doc": Select(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'disabled': 'disabled',
                'placeholder': 'Документ Основание'

            }),
            "status": Select(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'placeholder': 'Статус ДТП'
        }),



            "dtp_pos": Select(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'disabled': 'disabled',
                'placeholder': 'Документ Постановление'
            }),
            "file_doc": FileInput(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'placeholder': 'Прикрепить'
            }),
            "file_pos": FileInput(attrs={
                'class': 'form-control',
                'readonly': 'True',
                'placeholder': 'Прикрепить'
            }),

            # "Comment": TextInput(
            #     attrs={'class': 'form-control',
            #            'placeholder': 'Комментарий'
            #            }),

        }
