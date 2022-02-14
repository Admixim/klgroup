from django.shortcuts import render
from  price.models import Bank_pay,Price,Contract

from django.forms import ModelForm,TextInput,Textarea,DateInput,Select


class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ["id","name","price","extra_charge","comment","date","code_name"
                  ]


# class Assignment_payForm(ModelForm):
#     class Meta:
#         model = Price
#         fields = ["id",
#         "company", "summa","pay_number","pay_date","bank_pay_pdf","comment",
#                   ]

