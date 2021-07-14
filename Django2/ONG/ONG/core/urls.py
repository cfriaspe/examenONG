from django import urls
from django.urls import path
from .views import inicio,nosotros,perros,gatos,formulario, proveedor,modificar_proveedor, eliminar_proveedor
from .import views

urlpatterns = [

    path('', inicio, name="inicio"),
    path('index/', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('perros/', perros, name="perros"),
    path('gatos/', gatos, name="gatos"),
    path('formulario/', formulario, name="formulario"),
    path('proveedor/',proveedor, name="listado-proveedor"),
    path('registroproveedor/',views.nuevo_proveedor),
    path('modificar/<rut>/',modificar_proveedor, name="modificar_proveedor"),
    path('eliminar/<rut>/',eliminar_proveedor, name="eliminar_proveedor"),
]