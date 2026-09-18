from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('vista1/', views.vista1_app1, name='vista1_app1'),
    path('vista2/', views.vista2_app1, name='vista2_app1'),
]

