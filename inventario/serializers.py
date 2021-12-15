from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('codigo', 'nombre_producto', 'descripcion_producto', 'stock', 'precio')