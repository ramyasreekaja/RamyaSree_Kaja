from django.urls import path
from . import views


urlpatterns = [
    path('', views.linkup_list, name='linkup_list'),
    path('contact/', views.linkup_form, name='linkup_form'),
     path('contact/create/', views.linkup_form, name='linkup_create'),
    path('contact/<int:id>/', views.linkup_detail, name='linkup_detail'),
    path('contact/<int:id>/edit/', views.linkup_edit, name='linkup_update'),
    path('contact/<int:id>/delete/', views.linkup_delete, name='linkup__confirm_delete'),
]