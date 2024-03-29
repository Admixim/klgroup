from django.shortcuts import render
from .models import Client, Company, Partner, FilePerson, FileCompany
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


class PartnerForm(ModelForm):
    """Форма  тип участия  в ДТП"""

    class Meta:
        model = Partner
        fields = ['status',
                  'type',
                  'client',
                  'car',

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
    """Форма клиента"""

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
            "serial_pass": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия паспорта'
            }),
            "number_pass": NumberInput(attrs={
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
            "phone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "data_create": DateInput(format='%d/%m/%Y', attrs={
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
            "serial_lic": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия'
            }),
            "number_lic": NumberInput(attrs={
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
            "create_lic": DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи',
                'data-date-container': '#datepicker2',
                'data-provide': 'datepicker',
                'data-date-autoclose': 'true',
                'data-date-format': 'dd/mm/yyyy',
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
            "StatusCompany",
            "site_url",
            "number_phone",
            "mail_adress",
            "director_name",
            "bank_name",
            "bank_bik",
            "bank_adress",
            "bank_invoice",
            "bank_edit_invoice",

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
            "nalog_number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ИНН'
            }),
            "StatusCompany":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Статус контрагента'}),
            "nalog_main": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ОГРН'
            }),
            "nalog_registr": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'КПП'
            }),
            "company_adress": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес юридический'
            }),
            "number_phone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес эл.почты'
            }),
            "site_url": URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на сайт'
            }),
            "mail_adress": EmailInput(
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
            "bank_bik": NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'БИК банка'
                       }),
            "bank_adress": TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Юр.адрес банка'
                       }),
            "bank_invoice": NumberInput(
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


class FileCompanyForm(ModelForm):
    class Meta:
        model = FileCompany
        fields = ["id",
                  "files_comp",
                  "types",
                  "description",
                  "scan_doc",

                  ]

        widgets = {

            "files_comp": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Физ лицо'
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


class FilePersonForm(ModelForm):
    class Meta:
        model = FilePerson
        fields = ["id",
                  "files_person",
                  "types",
                  "description",
                  "scan_doc",


                  ]

        widgets = {

            "files_person": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Физ лицо'
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


FileCompanyFormset = modelformset_factory(
    FileCompany,
    fields=('files_comp', 'types', 'description', 'scan_doc',),
    extra=1,
    widgets={
        'files_comp': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Файл Юр.лица'
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
                'placeholder': 'Файл'
            }
        ),
    }
)

FilePersonFormset = modelformset_factory(
    FilePerson,
    fields=('files_person', 'types', 'description', 'scan_doc',),
    extra=1,
    widgets={
        'files_person': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Файл физ.лица'
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
                'placeholder': 'Файл'
            }
        ),
    }
)
