from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Servicio
from .forms import ProveedorFormulario

# Create your views here.

def inicio (request):
    return render(request,'core/index.html')

def nosotros (request):
    return render(request,'core/nosotros.html')

def perros (request):
    return render(request,'core/perros.html')

def gatos (request):
    return render(request,'core/gatos.html')

def formulario (request):
    return render(request,'core/formulario.html')

def registroprov (request):
    return render(request,'core/registroprov.html')

def proveedor (request):
    proveedor= Proveedor.objects.all()
    return render(request, 'core/proveedor.html', {'proveedor': proveedor})

def nuevo_proveedor(request):
    datos = {
        'form': ProveedorFormulario()
    }
    if request.method == 'POST':
        nuevoProveedor = ProveedorFormulario(data=request.POST)
        if nuevoProveedor.is_valid():
           nuevoProveedor.save()
           datos['mensaje'] = "Guardado"
        else:
            datos["form"] = ProveedorFormulario
    
    return render(request, 'core/registroproveedor.html', datos)

def modificar_proveedor(request, rut):
    
    proveedor = get_object_or_404(Proveedor, rut=rut)
    
    datos = {
        'form': ProveedorFormulario(instance=proveedor)
    }
    if request.method == 'POST':
        modificarProveedor = ProveedorFormulario(data=request.POST, instance=proveedor)
        if modificarProveedor.is_valid():
           modificarProveedor.save()
           return redirect(to="listado-proveedor")
        datos["form"] = modificarProveedor
    return render(request, 'core/modificar.html', datos)

def eliminar_proveedor(request, rut):

    proveedor = get_object_or_404(Proveedor, rut=rut)
    proveedor.delete()
    return redirect(to="listado-proveedor")





#def nuevo_proveedor(request):
#    datos = {
#        'form': ProveedorFormulario()
#    }
#    if request.method == 'POST':
#        nuevoProveedor = ProveedorFormulario(request.POST)
#        if nuevoProveedor.is_valid():
#           nuevoProveedor.save()
#           datos['mensaje'] = "guardado"
    
#    return render(request, 'core/test.html', datos)

#def nuevo_proveedor(request):
 #   proveedor = Proveedor()

  #  if request.method == 'POST':
  #      nuevoProveedor = ProveedorFormulario(request.POST, instance=proveedor)
  #      nuevoProveedor.save() 
  #      proveedor= Proveedor.objects.all()
  #      return render(request, 'core/proveedor.html', {'proveedor':proveedor})
  #  else:
  #      formulario = ProveedorFormulario()
  #      return render(request, 'core/test.html', {'formulario': formulario})


       
