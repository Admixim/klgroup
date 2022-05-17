from django.urls import path
from .views import *

urlpatterns = [
    path('', court_list, name='court-list'),
    path('court-new/', court_new, name='court-new'),
    path('court-new-pk/<int:pk>/', court_new_pk, name='court-new-pk'),
    path('court-event-add/<int:pk>/', court_event_add, name='court-event-add'),
    path('court-info-edit/<int:pk>/', court_info_edit, name='court-info-edit'),
    path('court-new/price-court-cash-new', price_court_cash_new, name='price-court-cash-new'),

    path('court-list-doc/', court_list_doc, name='court-list-doc'),

    # path('edit/<int:pk>/', views.accident_edit, name='court-edit'),
]
