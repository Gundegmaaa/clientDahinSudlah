from django.urls import path

from . import views

app_name = "worker_app"

urlpatterns = [
    path("", views.worker, name="worker"),
    path("create/", views.worker_add, name="worker_add"),
    path("edit/<int:id>/", views.worker_edit, name="worker_edit"),
    path("delete/<int:id>/", views.worker_delete, name="worker_delete"),
]

