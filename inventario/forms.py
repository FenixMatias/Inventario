from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ['codigo', 'nombre_producto', 'descripcion_producto', 'stock', 'precio']