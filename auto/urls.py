from django.urls import path
from . import views


urlpatterns = [
    path('', views.auto_list, name='auto-list'),
    path('auto-new/', views.auto_new, name='auto-new'),
    path('edit-auto-new/<int:pk>/', views.edit_auto_new, name='edit-auto-new'),
    path('edit/<int:pk>/', views.auto_edit, name='auto-edit'),
    # path('files-new/', views.files_new, name='files-new'),

]

