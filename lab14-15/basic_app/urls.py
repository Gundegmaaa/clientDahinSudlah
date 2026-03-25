from django.urls import path

from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.ClubListView.as_view(), name='list'),
    path('create/', views.ClubCreateView.as_view(), name='create'),
    path('update/<pk>/', views.ClubUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.ClubDeleteView.as_view(), name='delete'),
    path('<pk>/', views.ClubDetailView.as_view(), name='detail'),
]
