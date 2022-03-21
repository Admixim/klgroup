from django.contrib import admin
from client.models import *
from django.contrib.auth.models import Group, User

"""Отключение пользователей в админ панели"""
admin.site.unregister(User)
admin.site.unregister(Group)


class InFilesClient(admin.StackedInline):
    """Таблица с  файлами физ лица """

    model = FilePerson
    show_change_link = True
    extra = 0
    fieldsets = (
        ('Вложенные файлы', {
            'fields': (
                ("types", ("files_person"),
                 ),
                ("description", "scan_doc"),
            )
        }
         ),)


class InFilesComp(admin.StackedInline):
    """Таблица прикрепелнными файлами документов Юр. лиц """

    model = FileCompany
    show_change_link = True
    extra = 0

    fieldsets = (
        ('Вложенные файлы', {
            'fields': (
                ("types", ("files_comp"),
                 ),
                ("description", "scan_doc"),
            )
        }
         ),)


@admin.register(FilePerson)
class FileAdmin(admin.ModelAdmin):
    """Таблица прикрепелнными файлами документов Физ лиц """

    list_display = (
        "id",
        "files_person",
        "types",
        "description",
        "scan_doc",
        "created",
        "updated",
    )
    list_display_links = ("id", "description",)
    save_on_top = True
    search_fields = ("id", "description",)


@admin.register(FileCompany)
class FileAdmin(admin.ModelAdmin):
    """Таблица прикрепелнными файлами документов Юр.лиц """

    list_display = (
        "id",
        "files_comp",
        "types",
        "description",
        "scan_doc",
        "created",
        "updated",
    )
    list_display_links = ("id", "description",)
    save_on_top = True
    search_fields = ("id", "description",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Таблица статусов  сторон дела"""
    list_display = (
        "id",
        "name",
        "comment",
        "created",
        "updated",)
    list_display_links = ("id", "comment")
    list_filter = ("id",)
    search_fields = ("id",)


class InPartner(admin.StackedInline):
    model = Partner
    show_change_link = True
    extra = 0
    classes = ['collapse']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """Таблица статусов заявок с сайта в админ панели"""
    list_display = (
        "id",
        "status",
        "type",
        "comment",
        "created",
        "updated",)
    list_display_links = ("status", "type", "comment")
    list_filter = ("id", "status",)
    search_fields = ("id", "status",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Таблица основных данных о клиенте в  админ панели """

    list_display = (
        "id",
        "name",
        "surname",
        "midlename",
        "phone",
        "post_mail",
        "attorney",
        "doc_attorney",
        "date_birth",
        "doc_requisites",
        "link_social",
        "draft",
        "updated",
        "created")
    list_display_links = ("id", "name", "surname", "phone", "midlename")
    save_on_top = True
    inlines = [InFilesClient]
    search_fields = ("id", "name", "surname", "phone")

    fieldsets = (
                    ('Клиент', {
                        'fields': ((
                                    "name",
                                    "surname",
                                    "midlename"),)
                    },

                     ),
                    ('Контакты', {
                        "classes": ("collapse",),
                        'fields': ( (("phone","phone2"),
                                     ("post_mail", "link_social"),))
                    },

                     ),
                    ('Паспортные данные', {
                        "classes": ("collapse",),
                        'fields': ((("serial_pass", "number_pass"),
                                    ("enter_org", "data_create"),
                                    "date_birth",
                                    "point_birth",
                                    "adress_reg",
                                    "adress_home",
                                    "doc_pass",
                                    ))
                    },

                     ),
                    ('Водительское удостоверение', {
                        "classes": ("collapse",),
                        'fields': (
                        (("serial_lic", "number_lic"),
                         ("enter_lic", "create_lic"),
                         ("adress_lic", "category"),
                         "doc_lic",
                         ))
                    },

                     ),
                    ('Доверенность, банковские реквизиты', {
                        "classes": ("collapse",),
                        'fields': (
                            ("attorney",
                             "doc_attorney",
                             "doc_requisites",
                             ))
                    },

                     ),
                )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Таблица основных данных о Контрагенте в  админ панели """

    list_display = (
                "id",
                "name",
                "full_name",
                "nalog_number",
                "nalog_main",
                "nalog_registr",
                "company_adress",
                "number_phone",
                "mail_adress",
                "director_name",
                "doc_image",
                "site_url",
                "number_phone",
                "mail_adress",
                "director_name",
                "bank_name",
                "bank_bik",
                "bank_adress",
                "bank_invoice",
                "Comment",
                "bank_edit_invoice",
                "created",
                "is_active",

                "updated")
    list_display_links = ("id", "name", "full_name", "nalog_number")
    search_fields = ("id", "name", "full_name", "nalog_number",)
    save_on_top = True
    inlines = [InFilesComp]
