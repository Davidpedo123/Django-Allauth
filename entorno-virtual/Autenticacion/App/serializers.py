from rest_framework import serializers
from .models import Producto, ProductsDescuento

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'UnitsInStock', 'precio', 'imagen']
class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsDescuento
        fields = ['nombre', 'precio', 'Discontinued', 'imagen']