from django.urls import path
from .views import *
from price.urls import *
from expert.urls import *




urlpatterns = [
    #Список ДТП
    path('', accident_list, name='accident-list'),

    #Создание  нового дела о ДТП
    path('accident-new/', accident_new, name='accident-new'),
    # Добавлние участников в ДТП
    path('accident-add-partner/<int:accident_pk>/', accident_edit, name='accident-edit-add'),

    #Редактирования дела о  ДТП
    path('edit/<int:pk>/', accident_add_partner, name ='accident-edit'),

    #Список участнков  ДТП в деле о ДТП
    path('accident-list-doc/', accident_list_doc, name='accident_list_doc'),

    path('test/', test),


]
