from django.urls import path
from . import views


urlpatterns = [
    path('', views.linkup_list, name='linkup_list'),
    path('contact/', views.linkup_form, name='linkup_form'),
    path('create/', views.linkup_create, name='linkup_create'),
    #path('contact/create/', views.linkup_create, name='linkup_create'),
    path('contact/<int:id>/', views.linkup_detail, name='linkup_detail'),
    path('edit_contact/<int:id>/', views.linkup_update, name='linkup_update'),
    #path('contact/<int:id>/', views.linkup_view, name='linkup_view'),
    path('contact/<int:contact_id>/confirm_delete/', views.linkup_confirm_delete, name='linkup_confirm_delete'),
]
