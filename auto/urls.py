from django.urls import path
from auto.views import *


urlpatterns = [
    path('', auto_list, name='auto-list'),
    path('auto-new/', auto_new, name='auto-new'),
    path('edit-auto-new/<int:pk>/', edit_auto_new, name='edit-auto-new'),
    path('edit/<int:pk>/', auto_edit, name='auto-edit'),
    path('edit/model/', auto_model, name='auto-model'),
    # path('files-new/', files_new, name='files-new'),

]

