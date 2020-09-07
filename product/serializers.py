from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):


    
    class Meta:
        model = Producto
        fields = '__all__'
        

    def create(self, validate_data):
        instance = Producto()
        instance.marca = validate_data.get('marca')
        instance.alcohol = validate_data.get('alcohol')
        instance.mililitros = validate_data.get('mililitros') 
        print(validate_data.get('mililitros')) 
        instance.artesanal = validate_data.get('artesanal')
        instance.nacionalidad = validate_data.get('nacionalidad')
        instance.save()
        return instance
    
    def validate_marca(self, data):
        marcas = Producto.objects.filter(marca=data)
        if len(marcas) != 0:
            raise serializers.ValidationError("Este nombre ya existe")
        else:
            return data
    
    def validate_alcohol(self, value):
        if value <= 1:
            raise serializers.ValidationError("Poco Alcohol")
        else:
            return value
        

            
