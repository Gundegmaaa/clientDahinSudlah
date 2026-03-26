from django.urls import path

from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/add/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
]
