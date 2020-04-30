from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente

RUTA = 'http://restburgerapi.herokuapp.com'

class HamburguesasApiView(APIView):

    def get(self, request):

        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many = True)
        for i in range(len(serializer.data)):
            for j in range(len(serializer.data[i]['ingredientes'])):
                iden = serializer.data[i]['ingredientes'][j]
                serializer.data[i]['ingredientes'][j] = {'path': f'{RUTA}/ingrediente/{iden}'}
        return Response({'message': "Hamburguesas", 'body': serializer.data}, status = status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = HamburguesaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Hamburguesa creada con éxito", 'body': serializer.data}, status = status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HamburguesaApiView(APIView):

    def get(self, request, id):
        if not id.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            hamburguesa = Hamburguesa.objects.get(id = id)
            serializer = HamburguesaSerializer(hamburguesa)
            print(serializer.data['ingredientes'])
            for i in range(len(serializer.data['ingredientes'])):
                iden = serializer.data['ingredientes'][i]
                serializer.data['ingredientes'][i] = {'path': f'{RUTA}/ingrediente/{iden}'}
            return Response({'message': "Hamburguesa", 'body': serializer.data}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "El objeto no existe"}, status=404)
            

    def delete(self, request, id):
        if not id.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            hamburguesa = Hamburguesa.objects.get(id = id)
            hamburguesa.delete()
            return Response({'message': "Hamburguesa borrada con éxito"}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "El objeto no existe"}, status=404)
    
    def patch(self, request, id):
        if not id.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            hamburguesa = Hamburguesa.objects.get(id = id)
            serializer = HamburguesaSerializer(hamburguesa, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': "Hamburguesa modificada con éxito", 'body': serializer.data}, status = status.HTTP_200_OK)
            else:
                return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "El objeto no existe"}, status=404)
        

class IngredientesApiView(APIView):

    def get(self, request):

        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many = True)
        return Response({'message': "Ingredientes", 'body': serializer.data}, status = status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = IngredienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Ingrediente creado con éxito", 'body': serializer.data}, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredienteApiView(APIView):

    def get(self, request, id):
        if not id.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ingrediente = Ingrediente.objects.get(id = id)
            serializer = IngredienteSerializer(ingrediente)
            return Response({'message': "Ingrediente", 'body': serializer.data}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "El objeto no existe"}, status=404)

    def delete(self, request, id):
        if not id.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ingrediente = Ingrediente.objects.get(id = id)
            hamburguesas = Hamburguesa.objects.filter(ingredientes__id = id).count()
            if hamburguesas > 0:
                return Response({'message': "El ingrediente no puede ser borrado, está en alguna hamburguesa"}, status = 403)
            else:
                ingrediente.delete()
                return Response({'message': "Ingrediente borrado con éxito"}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "El objeto no existe"}, status=404)

    def patch(self, request, id):
        if not id.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ingrediente = Ingrediente.objects.get(id = id)
            serializer = IngredienteSerializer(ingrediente, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': "Ingrediente modificado con éxito", 'body': serializer.data}, status = status.HTTP_200_OK)
            else:
                return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "El objeto no existe"}, status=404)

class HamburguesasIngredientesApiView(APIView):

    def get(self, request, id_h, id_i):
        if not id_h.isdigit() or not id_i.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            hamburguesa = Hamburguesa.objects.get(id = id_h)
            serializer = HamburguesaSerializer(hamburguesa)
            print(serializer.data['ingredientes'])
            for i in range(len(serializer.data['ingredientes'])):
                iden = serializer.data['ingredientes'][i]
                serializer.data['ingredientes'][i] = {'path': f'{RUTA}/ingrediente/{iden}'}
            return Response({'message': "Hamburguesa", 'body': serializer.data}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "El objeto no existe"}, status=404)

    def put(self, request, id_h, id_i):
        if not id_h.isdigit() or not id_i.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            hamburguesa = Hamburguesa.objects.get(id = id_h)
            ingrediente = Ingrediente.objects.get(id = id_i)
            hamburguesa.ingredientes.add(ingrediente)
            hamburguesa.save()
            return Response({'message': "El ingrediente ha sido agregado con éxito"}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "Uno o ambos objetos no existen"}, status=404)

    def delete(self, request, id_h, id_i):
        if not id_h.isdigit() or not id_i.isdigit():
            return Response({"message": "La request no es válida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            hamburguesa = Hamburguesa.objects.get(id = id_h)
            ingrediente = Ingrediente.objects.get(id = id_i)
            hamburguesa.ingredientes.remove(ingrediente)
            hamburguesa.save()
            return Response({'message': "El ingrediente ha sido removido con éxito"}, status = status.HTTP_200_OK)
        except:
            return Response({"message": "Uno o ambos objetos no existen"}, status=404)

        

