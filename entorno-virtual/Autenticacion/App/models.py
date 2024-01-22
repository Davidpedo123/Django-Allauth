

# Create your models here.
# en myapp/models.py
from django.db import models
from django.db import connections
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    UnitsInStock = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=40000)

    @classmethod
    def obtener_productos_northwind(cls):
        with connections['northwind'].cursor() as cursor:
            cursor.execute("SELECT ProductName, UnitPrice, UnitsInStock, imagen FROM Products WHERE CategoryID = 1;")  # Modificado para incluir 'imagen'
            results = cursor.fetchall()

        productos_northwind = []
        for result in results:
            nombre, precio, unidades_en_stock, imagen = result  # Modificado para incluir 'imagen'
            productos_northwind.append(cls(nombre=nombre, UnitsInStock=unidades_en_stock, precio=precio, imagen=imagen))  # Modificado para incluir 'imagen'

        return productos_northwind
class ProductsDescuento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Discontinued = models.DecimalField(max_digits=10, decimal_places=2)  # Mantén el tipo de datos Decimal
    imagen = models.CharField(max_length=40000)
    
    @classmethod
    def ObtenerDescuentosDef(cls):
        with connections['northwind'].cursor() as cursor:
            cursor.execute("SELECT ProductName, UnitPrice, Discontinued, imagen FROM Products WHERE Discontinued > 1;")
            results = cursor.fetchall()

        productos_northwind_discon = []
        for result in results:
            nombre, precio, discontinued, imagen = result
            productos_northwind_discon.append(cls(nombre=nombre, precio=precio, Discontinued=discontinued, imagen=imagen))
       
        return productos_northwind_discon
