from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#from core.models import Animal
#from .serializers import AnimalSerializer
from core.models import Proveedor
from .serializers import ProveedorSerializer

#@csrf_exempt
#@api_view(['GET'])
#def lista_animal(request):
#    usuario = Animal.objects.all()
#    serializers = AnimalSerializer(usuario, many=True)
#    return Response(serializers.data)

@csrf_exempt
@api_view(['GET'])
def lista_proveedor(request):
    usuario = Proveedor.objects.all()
    serializers = ProveedorSerializer(usuario, many=True)
    return Response(serializers.data)    

#@csrf_exempt
#@api_view(['POST'])
#def modificar_animal(request):
#    if request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = AnimalSerializer(data = data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

@csrf_exempt
@api_view(['POST'])
def modificar_proveedor(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)                

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def detalle_proveedor(request,id):
    try:
        proveedor = Proveedor.objects.get(rut=id)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =ProveedorSerializer(proveedor)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(proveedor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)