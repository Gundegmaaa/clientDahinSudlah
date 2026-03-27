from django.urls import path

from . import views

urlpatterns = [
    path("", views.zodiac_list, name="zodiac_list"),
    path("<int:zodiac_id>/", views.zodiac_detail, name="zodiac_detail"),
]
