from django.contrib import admin
from expert.models import Expert, ExpertComp, Type, ExpertFiles

class InFiles(admin.StackedInline):
    model = ExpertFiles
    show_change_link = True
    extra = 0
    fieldsets = (
        ('Вложенные файлы', {
            'fields': (
                ("types", ("files"),
                 ),
                ("description", "scan_doc"),
            )
        }
         ),)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Таблица Видов экспертизы """

    list_display = (
        "id",
        "name",
        "comment",
    )
    list_display_links = ("id", "name",)
    save_on_top = True
    search_fields = ("id", "name",)
    save_on_top = True

@admin.register(ExpertComp)
class ExpertCompAdmin(admin.ModelAdmin):
    """Таблица Организаций экспертных  в  админ панели """

    list_display = (
        "id",
        "name",
        "comment",
        "mail_post",)
    list_display_links = ("id", "name", "mail_post",)
    save_on_top = True
    search_fields = ("id", "name",)
    save_on_top = True





@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    """Таблица основных данных о клиенте в  админ панели """

    list_display = (
        "id",
        "num_doc",
        "summa_exp",
        "price_nwear",
        "price_wwear",
        "price_mmarket",
        "price_uleftovers",
        "price_summa",
        ("client"),
        ("contragent"),
        ('accident'),
        ('type'),
        "data_in",
        "data_out",
        "comment",
        "price_uts",
        "updated",
        "created",)
    list_display_links = ("id", "num_doc",)
    save_on_top = True
    inlines = [InFiles]
    search_fields = ("id",)
    save_on_top = True


class InExpert(admin.StackedInline):
    model = Expert
    show_change_link = True
    extra = 0
    classes = ['collapse']
    fieldsets = (
        ('Оперция оценки', {
            "classes": ("collapse",),
            'fields': (
                ("num_doc",
                 ("contragent"),
                 "summa_exp",
                 ('type'),
                 ('accident')),
                ("data_in",
                 "data_out"),
                ("price_nwear", "price_wwear"),
                ("price_mmarket", "price_uleftovers",),
                ("price_summa", "price_uts")
            )
        }
         ),
        ('Комментарий', {
            "classes": ("collapse",),
            'fields': (("comment",
                        ))

        }
         ),
    )
