from django.contrib import admin
from accident.models import *
from crm_kl.models import *


# Register your models here.
admin.site.site_title = "KL Group"
admin.site.site_header = "KL Group"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug','is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


#
# @admin.register(responsible)
# class responsibleAdmin(admin.ModelAdmin):
#     """Ответственный """
#     list_display = (
#         "id", "name", "full_name", "is_active", "created", "updated")
#     save_on_top = True
#     search_fields = ("id", "name")


# @admin.register(client_pay)
# class ClientPayAdmin(admin.ModelAdmin):
#     """Таблица основных данных о клиенте в  админ панели """
#     # contract, plaintiff, car_plaintiff, culprit, car_culprit, responsible, pay_method
#     list_display = ("id", "number",('contract'),('plaintiff')
#                  ('culprit'), ('car_culprit'), "responsible", "pay_method",)
#     save_on_top = True
#     search_fields = ("id", "number")
#     list_display_links = ("id", "number","car_plaintiff","plaintiff")
#     # inlines = [InExpert, InCourt]
#     readonly_fields = ['get_culprit', 'get_plaintiff', 'get_car_plaintiff', 'get_car_culprit']
#
#     fieldsets = (
#         ('Данные ДТП', {
#             "classes": ("collapse",),
#             'fields': ("number", "location_accident", ("data", "time"), ("dtp_doc", "doc"), ("dtp_pos", "doc_1")
#                        ),
#
#         },
#
#          ),
#         ('Данные истца', {
#             "classes": ("collapse",),
#             'fields': (("plaintiff", "get_plaintiff"), ("car_plaintiff", "get_car_plaintiff"))
#         }
#          ),
#         ('Данные ответчика', {
#             "classes": ("collapse",),
#             'fields': (("culprit", "get_culprit"), ("car_culprit", "get_car_culprit")),
#
#         }
#          ),
#
#         ('Данные по судебному делу', {
#             'fields': ("location_court", "data_reg", "uid_number", "case_number",("doc_isk","doc_pos","doc_spr","doc_dtp")),
#
#         }
#          ),
#     )
#
#     def get_culprit(self, obj):
#         return '+7{} '.format(obj.culprit.phone)
#     get_culprit.short_description = "Контактный номер"
#
#     def get_plaintiff(self, obj):
#         return '+7{} '.format(obj.plaintiff.phone)
#     get_plaintiff.short_description = "Контактный номер"
#
#     def get_car_plaintiff(self, obj):
#         print(self, obj)
#         return obj.car_plaintiff.insurance_company
#     get_car_plaintiff.short_description = "СК"
