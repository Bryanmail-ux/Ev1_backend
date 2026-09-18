from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inicio'
urlpatterns = [path('', views.inicio, name='inicio')]
urlpatterns = [
    path('admin/', admin.site.urls),
]