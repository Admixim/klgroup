from django.urls import path
from .views import *


urlpatterns = [
    path('', court_list, name='court-list'),
    path('court-new/', court_new, name='court-new'),
    path('court-new/price-court-cash-new', price_court_cash_new, name='price-court-cash-new'),
    path('court-edit/<int:pk>/', court_edit, name='court-edit'),
    path('court-list-doc/', court_list_doc, name='court-list-doc'),

    # path('edit/<int:pk>/', views.accident_edit, name='court-edit'),
]