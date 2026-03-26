from django.urls import path
from . import views

app_name = 'branch_app'

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('add/', views.branch_create, name='branch_create'),
    path('edit/<int:pk>/', views.branch_update, name='branch_update'),
    path('delete/<int:pk>/', views.branch_delete, name='branch_delete'),
]
