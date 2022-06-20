from django.contrib import admin
from auto.models import Car, Brend, Model, AutoFiles, Insurance


class InFiles(admin.StackedInline):
    model = AutoFiles
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


@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    """Таблица Марок ТС """

    list_display = (
        "id",
        "name",
        "is_active",
        "updated",
        "created"
    )
    list_display_links = ("id", "name")
    save_on_top = True
    search_fields = ("id", "name",)


@admin.register(AutoFiles)
class FileAdmin(admin.ModelAdmin):
    """Таблица прикрепелнными файлами документов """

    list_display = (
        "id",
        "files",
        "types",
        "description",
        "scan_doc"
    )
    list_display_links = ("id", "description")
    save_on_top = True
    search_fields = ("id", "description",)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    """Таблица Моделей ТС """

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "category":
    #         kwargs["queryset"] = Brend.objects.filter(name__in=Model)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = (
        "id",
        "name",
        "brand_auto",
        "is_active",
        "updated",
        "created"
    )
    list_display_links = ("id", "name")
    save_on_top = True
    search_fields = ("id", "name",)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    """Таблица данных страховых полисов ТС"""

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "category":
    #         kwargs["queryset"] = Brend.objects.filter(name__in=Model)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = (
        "id",
        "types",
        "i_serial",
        "i_number",
        "start_date",
        "end_date",
        "description",
        "author",
        "updated",
        "created"
    )
    list_display_links = ("id",)
    save_on_top = True
    search_fields = ("id", "i_number",)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Таблица основных данных о клиенте в  админ панели """

    list_display = (
        "id",
        "model",
        "marka",
        "number",
        "color",
        "sts_s",
        "pts_s",
        "date_made",
        "pts_n",
        "Comment",
        "sts_n",
        "driver",
        "updated",
        "created")
    list_display_links = (
        "id",
        "model",
        "marka",
        "number",
        "color",
        "date_made",
        "driver")
    save_on_top = True
    search_fields = ("id", "number", "driver")
    inlines = [InFiles]
    fieldsets = (
        ('ТС', {
            'fields': (("model",
                        "marka",
                        "number",
                        "color",
                        "date_made"),)
        },

         ),
        ('Документ ТС', {
            'fields': ((("sts_s", "sts_n", "sts_date",),
                        ("pts_n", "pts_s", "pts_date",),
                        "vin",))
        },

         ),
        ('Водительское удостоверение', {
            'fields': (
                ("driver",
                 ))
        },

         ),

    )
