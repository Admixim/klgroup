from django.shortcuts import render
from .models import Client, Company, Partner

from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, EmailInput, URLInput, FileField, URLField, EmailField, \
    IntegerField


class PartnerForm(ModelForm):
    # Форма  тип участия  в ДТП
    class Meta:
        model = Partner
        fields = ['status',
                  'type',
                  # 'accident',
                  'client',
                  'car',
                  # 'comment',
                  ]

        widgets = {
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус в ДТП'
            }),
            "accident": Select(attrs={
                'class': 'form-control',
                'placeholder': 'ДТП'
            }),
            "client": Select(attrs={
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
                'placeholder': 'Физ лицо'
            }),
            "car": Select(attrs={
                'class': 'form-control select2 select2-hidden-accessible',
                'data-select2-id': '1',
                'tabindex': '-1',
                'placeholder': 'ТС физ лица'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коментарий'
            }),
        }


class ClientForm(ModelForm):
    # Форма клиента

    class Meta:
        model = Client
        fields = [
            "name",
            "surname",
            "midlename",
            "serial_pass",
            "number_pass",
            "point_birth",
            "enter_org",
            "data_create",
            "adress_reg",
            "date_birth",
            "adress_home",
            "doc_pass",
            "serial_lic",
            "number_lic",
            "enter_lic",
            "create_lic",
            "adress_lic",
            "category",
            "post_mail",
            "link_social",
            "phone",
        ]

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
               ' data-parsley-min' : ' 6',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "midlename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "serial_pass": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия паспорта'
            }),
            "number_pass": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер паспорта'
            }),
            "enter_org": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Орган выдал документ'
            }),
            "post_mail": EmailInput(attrs={
                'class': 'form-control',
                'parsley-type' : "email",
                'placeholder': 'Эл.почта',
            }),
            "link_social": URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Соц.Адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "data_create": DateInput(format='%d/%m/%Y',attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
            }),
            "date_birth": DateInput(format='%d/%m/%Y', attrs={
                    'class': 'form-control',
                    'placeholder': 'Дата  рождения',
                    'data-date-container': '#datepicker2',
                    'data-provide': 'datepicker',
                    'data-date-autoclose': 'true',
                    'data-date-format': 'dd/mm/yyyy',

                }),
            "point_birth": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место рождение'
            }),
            "adress_reg": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес регистрации'
            }),
            "adress_home": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Факт адрес'
            }),
            "serial_lic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия'
            }),
            "number_lic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),
            "enter_lic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кем выдан'
            }),
            "adress_lic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место выдачи'
            }),
            "category ": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категории прав'
            }),
            "create_lic": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
            }),

        }


class CompanyForm(ModelForm):
    """Форма контрагента"""

    class Meta:
        model = Company
        fields = [
            "name",
            "full_name",
            "nalog_number",
            "nalog_main",
            "nalog_registr",
            "company_adress",
            "site_url",
            "number_phone",
            "mail_adress",
            "director_name",
            "bank_name",
            "bank_bik",
            "bank_adress",
            "bank_invoice",
            "bank_edit_invoice",
            "doc_image",
        ]

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование компании'
            }),
            "full_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полное наименование компании'
            }),
            "nalog_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ИНН'
            }),
            "nalog_main": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ОГРН'
            }),
            "nalog_registr": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'КПП'
            }),
            "company_adress": Textarea(attrs={

                'class': 'form-control',
                'placeholder': 'Адрес юридический'
            }),
            "number_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес эл.почты'
            }),
            "site_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на сайт'
            }),
            "mail_adress": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Эл.Почта'
                       }),
            "director_name": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Директор Ф.И.О'
                       }),
            "bank_name": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Наименование банка'
                       }),
            "bank_bik": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'БИК банка'
                       }),
            "bank_adress": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Юр.адрес банка'
                       }),
            "bank_invoice": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Расчетный счет'
                       }),
            "bank_edit_invoice": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Кор/счет'
                       }),
            "Comment": Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Комментарий'
                       }),

        }
