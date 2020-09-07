from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import filters


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    #Filtrado de back end por defecto--------
    filter_backends = [filters.SearchFilter]
    search_fields = ['=marca', '=nacionalidad']
    #----------------------------------------

    
    
    def post(self, request):
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Filtrado como endpoints-------------------------------------
class ProductViewSetMarca(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        queryset = Producto.objects.filter(marca=self.kwargs['marca'])
        return queryset


class ProductViewSetNacionalidad(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.filter(nacionalidad=self.kwargs['nacionalidad'])
        return queryset
#----------------------------------------------------------------


        



