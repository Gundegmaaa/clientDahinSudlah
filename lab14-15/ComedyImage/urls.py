from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from basic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('hello/', views.HelloDjangoView.as_view(), name='hello_django'),
    path('basic_app/', include('basic_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
