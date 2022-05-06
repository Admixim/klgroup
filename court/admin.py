import datetime
from django.contrib import admin
from court.models import *
from court.models import Procedure
from client.models import Company
from django.http import HttpResponseRedirect


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Таблица статус ДТП"""

    list_display = (
        "id",
        "name",
        "comment",
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id", "name")

@admin.register(judge_help)
class judgeHelpAdmin(admin.ModelAdmin):
    """Таблица с списком  помощников судей"""

    list_display = (
        "id",
        "name",
        "message",
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id", "name")


@admin.register(judge)
class judgeAdmin(admin.ModelAdmin):
    """Таблица с списком судей"""

    list_display = (
        "id",
        "name",
        "adress_mail",
        "contact_phone",
        ('judge_help'),
        "message",
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id", "name")


@admin.register(ListCourt)
class ListCourtAdmin(admin.ModelAdmin):
    """Таблица c списком судов КК"""

    list_display = (
        "id",
        "name",
        "adress",
        "adress_post",
        "adress_mail",
        "contact_phone",
        "message",
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id", "name")


@admin.register(worker)
class workerAdmin(admin.ModelAdmin):
    """Таблица с списком сотрудников"""

    list_display = (
        "name",
        "surname",
        "midlename",
        "phone",
        "post_mail",
        "work_mail",
        "link_social")
    save_on_top = True
    search_fields = ("id", "name")




@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    """Таблица с процедур  судебного дела"""

    list_display = (
        "id",
        "name",
        "message",
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id", "name")

@admin.register(ListEnd)
class ListEndAdmin(admin.ModelAdmin):
    """Список наменований для окончания сроков, вступления в силу документов"""

    list_display = (
        "id",
        "name",
        "message",
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id", "name")





class InCourt(admin.StackedInline):
    model = Court
    show_change_link = True
    extra = 0
    classes = ['collapse']

    # fieldsets = (
    #     ('Производство по делу', {
    #         "classes": ("collapse",),
    #         'fields': (
    #             ("procedure", "worker"),
    #             (("akt_end"), "data_finish"),
    #             ("curt_hall"),
    #             ("date_start", "date_stop"),
    #
    #         )
    #     }
    #      ),
    #     ('Комментарий1', {
    #         "classes": ("collapse",),
    #         'fields': ("message",
    #                    "file_paste",)
    #
    #     }
    #      ),
    #
    # )


@admin.register(Court)
class CurtAdmin(admin.ModelAdmin):
    """Таблица основных данных о Судебном процессе в  админ панели """

    list_display = (
        "id",
        ('procedure'),
        ('worker'),
        "data_finish",
        "file_paste",
        "date_start",
        "date_stop",
        ('akt_end'),
        "time_stop",
        "curt_hall",
        "message",

    )
    list_display_links = ("curt_hall", "procedure",)
    save_on_top = True

    fieldsets = (
            ('Временное окно', {
            "classes": ("collapse",),
            'fields': (
                ("procedure", "worker", "data_finish",),
                ("curt_hall"),
                ("date_start", "date_stop"),
                ("akt_end"),
                ("message", "file_paste",)
            )
        }
         ),
    )

@admin.register(InfoCourt)
class InfoCourtAdmin(admin.ModelAdmin):
    """Список наменований для окончания сроков, вступления в силу документов"""
    inlines = [
        InCourt,
    ]
    list_display = (
        "id",
        "case_number",
        "uid_number",
        "data_reg",
        ("location"),
        "is_active",
        "created",
        "updated")
    save_on_top = True
    search_fields = ("id",)
    list_display_links = ("id", "case_number")
