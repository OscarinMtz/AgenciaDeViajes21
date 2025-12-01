from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir todas las URLs de app_viajes desde la raíz
    path('', include('app_viajes.urls')),
]
