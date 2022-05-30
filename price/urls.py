from django.urls import path

from price.views import *




urlpatterns = [
    path('', price_list, name='price-list'),
    path('price_court_cash/<int:pk>/', price_court_cash, name='price-court-cash-accident'),
    # path('edit/<int:pk>/', views.price_edit, name='price-edit'),
    # path('expert_new/', views.price_new, name='price-new'),
    # path('bank_pay/', views.bank_pay_list, name='bank_pay-list'),
    # path('bank_pay_new/', views.bank_pay_new, name='bank_pay-new'),
    # path('bank_pay/edit/<int:pk>/', views.bank_pay_edit, name='bank_pay-edit'),
]
