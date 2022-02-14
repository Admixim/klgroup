from django.contrib import admin
from .models import Price,Bank_pay,Contract

# Register your models here.


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    """Таблица с  прайсом услуг"""
    list_display = ("id",
        "name","price","extra_charge","comment","date","code_name")
    save_on_top = True
    search_fields = ("id", "name")


@admin.register(Bank_pay)
class Bank_payAdmin(admin.ModelAdmin):
    """Таблица  данных цессий оплат"""
    list_display = ("id",
        ('company'), "summa","pay_number","pay_date","bank_pay_pdf","comment",)
    save_on_top = True
    search_fields = ("id", "pay_number")

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """"""
    list_display = ("id",('contragent'),('company'),
         "name","number","name","date","comment")
    save_on_top = True
    search_fields = ("id", "pay_number")
