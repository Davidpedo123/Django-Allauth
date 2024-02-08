from rest_framework import serializers
from .models import Producto, ProductsDescuento, OrdersForRegion

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'UnitsInStock', 'precio', 'imagen']
class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsDescuento
        fields = ['nombre', 'precio', 'Discontinued', 'imagen']
class OrderRegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrdersForRegion
        fields = ['total_orders', 'ShipRegion']