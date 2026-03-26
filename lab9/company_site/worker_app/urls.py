from django.urls import path
from . import views

app_name = 'worker_app'

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('add/', views.worker_create, name='worker_create'),
    path('edit/<int:pk>/', views.worker_update, name='worker_update'),
    path('delete/<int:pk>/', views.worker_delete, name='worker_delete'),
]
