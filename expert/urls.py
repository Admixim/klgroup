from django.urls import path
from .views import *

urlpatterns = [
    path('', expert_list, name='expert-list'),
    path('edit/<int:pk>/', expert_edit, name='expert-edit'),
    path('expert-new/', expert_new, name='expert-new'),
    path('expert-new-pk/<int:pk>/',  expert_new_pk, name='expert-new-pk'),
    path('expert-modal-new/', expert_modal_new, name='expert-modal-new'),


]
