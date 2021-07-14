#from django.urls import path
#from .views import lista_animal, modificar_animal, detalle_animal

#urlpatterns = [
#    path('lista_animal',lista_animal, name="lista_animal"),
#    path('modificar_animal',modificar_animal, name="modificar_animal"),
#    path('animal/<id>',detalle_animal, name="detalle_animal"),
#]

from django.urls import path
from .views import lista_proveedor, modificar_proveedor, detalle_proveedor

urlpatterns = [
    path('lista_proveedor',lista_proveedor, name="lista_proveedor"),
    path('modificar_proveedor',modificar_proveedor, name="modificar_proveedor"),
    path('proveedor/<id>',detalle_proveedor, name="detalle_proveedor"),
]