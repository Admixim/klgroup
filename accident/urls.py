from django.urls import path
from accident.views import *
from expert.urls import *




urlpatterns = [
    # Список ДТП
    path('', accident_list, name='accident-list'),

    # Создание  нового дела о ДТП
    path('accident-new/', accident_new, name='accident-new'),
    # Добавлние участников в ДТП
    # path('accident-add-partner/<int:accident_pk>/', accident_edit, name='accident-edit-add'),

    # Добавление участников   редактирование ДТП
    path('accident-add-partner/<int:pk>/', accident_add_partner, name='accident-edit'),

    # Список  документов о   ДТП в деле
    path('accident-list-doc/<int:pk>/', accident_list_doc, name='accident_list_doc'),

    path('test/', test),

    # Учебная страница по JS
    path('techerjs/', techerjs, name='techerjs'),



]
