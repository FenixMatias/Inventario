from django.db import models

# Create your models here.

class Producto(models.Model):
	codigo = models.AutoField(primary_key = True)
	nombre_producto = models.CharField(max_length=5000, blank = False, null = False)
	descripcion_producto = models.CharField(max_length=5000, blank = False, null = False)
	stock = models.IntegerField()
	precio =models.IntegerField()

	class meta:
		 verbose_name = 'Producto'
		 verbose_name_plural = 'Productos'
		 ordering = ['nombre_producto']


	def __str__(self):
		return self.nombre_producto
