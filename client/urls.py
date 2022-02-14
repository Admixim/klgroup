from django.urls import path
from . import views



urlpatterns = [
    path('', views.client_list, name='client-list'),
    path('client-new/', views.client_new, name='client-new'),
    path('edit/<int:pk>/', views.client_edit, name='client-edit'),
    path('company/', views.company_list, name='company-list'),
    path('company-new/', views.company_new, name='company-new'),
    path('company/edit/<int:pk>/', views.company_edit, name='company-edit'),

]
