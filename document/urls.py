from django.urls import path
from .views import *

urlpatterns = [
    # path('pdf/<pk>/', DocumentListView.as_view(), name='create-invoice'),
    # path('test/', DocumentListView, name='create-invoice1'),
    path('pdf_contract/<int:client_id>/', pdf_contract, name='pdf_contract'),
    path('pdf_contract_one/<int:client_id>/', pdf_contract_one, name='pdf_contract_one'),
    path('pdf_contract_one_add/<int:client_id>/', pdf_contract_one_add, name='pdf_contract_one_add'),
    path('pdf_assignment/<int:client_id>/', pdf_assignment, name='pdf_assignment'),
    path('pdf_assignment_add/<int:client_id>/', pdf_assignment_add, name='pdf_assignment_add'),
    path('pdf_contract_expert/<int:client_id>/', pdf_contract_expert, name='pdf_contract_expert'),
    path('pdf_contract_arbit/<int:client_id>/', pdf_contract_arbit, name='pdf_contract_arbit'),
    path('pdf_expert/<int:client_id>/', pdf_contract_expert, name='pdf_expert'),

    # path('contract/', contract, name='contract')
    # path('pdf/<int:pk>/', views.auto_edit, name='auto-edit'),
]
