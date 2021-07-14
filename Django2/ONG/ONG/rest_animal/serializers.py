from rest_framework import fields, serializers
from core.models import Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['rut','razon_social','descripcion','Servicio']