from django.urls import path

from . import views

app_name = "branch_app"

urlpatterns = [
    path("", views.salbar, name="salbar"),
    path("create/", views.salbar_add, name="salbar_add"),
    path("edit/<int:id>/", views.salbar_edit, name="salbar_edit"),
    path("delete/<int:id>/", views.salbar_delete, name="salbar_delete"),
]

