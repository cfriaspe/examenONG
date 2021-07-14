from django import forms
from django.forms import fields
from .models import Proveedor

class ProveedorFormulario(forms.ModelForm):
    class Meta: 
        model = Proveedor
        fields = ('rut', 'razon_social', 'descripcion', 'Servicio')