from django.contrib import admin
from .models import *
from expert.admin import InExpert
from court.admin import InCourt
from client.admin import InPartner


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Таблица статус ДТП"""
    list_display = (
        "name",
        "comment")
    save_on_top = True
    search_fields = ("id", "name")


@admin.register(AccidentPos)
class AccidentPosAdmin(admin.ModelAdmin):
    """Таблица Документ постановление ДТП"""

    list_display = (
        "id",
        "name",
        "full_name",)
    list_display_links = ("id", "name",)
    search_fields = ("id", "name",)
    save_on_top = True


@admin.register(AccidentDoc)
class AccidentDocAdmin(admin.ModelAdmin):
    """Таблица основных данных о ДТП  в  админ панели """

    list_display = (
        "id",
        "name",
        "full_name",)
    list_display_links = ("id", "name")
    search_fields = ("id", "name",)
    save_on_top = True


@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    """Таблица основных данных о клиенте в  админ панели """

    list_display = (
        "id",
        "number",
        ("court_info"),
        "data",
        "time",
        "location_accident",
        ('dtp_pos'),
        ('dtp_doc'),
        'status',
        "file_doc",
        "file_pos",
        "data_insurance",
        "slug",
        "message",)
    save_on_top = True
    search_fields = ("id", "number")
    list_display_links = ("id", "number",)
    inlines = [ InExpert, InPartner]
    # readonly_fields = [
    #
    #     'get_human',
    #     'get_car',
    #
    # ]
    fieldsets = (
        ('Данные ДТП', {
         'fields': (
                "number",

                "location_accident",
                "status","court_info",
                ("data", "time"),
                ("dtp_doc", "file_doc"),
                ("dtp_pos", "file_pos")
                ),
                        },
         ),



    #     ('Данные по судебному делу', {
    #      "classes": ("collapse",),
    #      'fields': (
    #          ("info_court"),
    #
    #             ),
    #      }
    #                 ),
    )
    #
    # def get_human(self, obj):
    #     return '+7{} '.format(obj.human.phone)
    # get_human.short_description = "Контактный номер"
    #
    #
    #
    # def get_car(self, obj):
    #     print(self, obj)
    #     return obj.car.insurance_company
    # get_car.short_description = "СК"




    # get_culprit.allow_tags = True


