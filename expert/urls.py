from django.urls import path
from expert import views

urlpatterns = [
    path('', views.expert_list, name='expert-list'),
    path('edit/<int:pk>/', views.expert_edit, name='expert-edit'),
    path('expert-new/', views.expert_new, name='expert-new'),
    path('expert-new-pk/<int:pk>/', views.expert_new_pk, name='expert-new-pk'),
    path('expert-modal-new/', views.expert_modal_new, name='expert-modal-new'),


]
