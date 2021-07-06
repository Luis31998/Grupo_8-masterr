from rest.serializers import ObraSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Obra

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
#Si request es por GET: accedimos a una URL para listar los elementos
#Si request es por POST; enviamos elementos a la vista(Por ejemplo desdeun formulario)
def lista_obras(request):
    if request.method == 'GET':
        #Listar las Obras desde la BD
        Obras = Obra.objects.all()
        serializer = ObraSerializer(Obras,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



#Si request es por GET: accedimos a una URL para ver el detalle de una obra
#Si request es por PUT: MODIFICAMOS LOS DATOS DE LA OBRA CUYA IDOBRA SE ENVIO POR LA URL
#Si request es DELETE: eliminamos obras cuyas id se envío por la URL
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_obras(request, id):
    try:
        obras = Obra.objects.get(idObra=id)

    except Obra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ObraSerializer(obras)
        return Response(serializer.data)


    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(obras,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        obras.delete()
        return Response(status.HTTP_204_NO_CONTENT)
