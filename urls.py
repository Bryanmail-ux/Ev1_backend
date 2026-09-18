from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('inicio.urls')),  # Ruta por defecto
    path('admin/', admin.site.urls),
    path('app2/', include('app2.urls')),
]