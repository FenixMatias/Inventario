from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProductoForm
from .models import Producto
from django.views.generic import TemplateView,ListView
from rest_framework import viewsets
from .serializers import ProductoSerializer


# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all().order_by('codigo')
	serializer_class = ProductoSerializer

class Inicio(TemplateView):
	template_name = 'index.html'

class CrearProductoAPI(TemplateView):
	template_name = 'Crear_ProductoAPI.html'

class VistaProductoClienteAPI(TemplateView):
	template_name = 'Vista_Producto_ClienteAPI.html'

class ListadoProducto(ListView):
	Model = Producto
	template_name = 'inventario/listar_producto.html'
	context_object_name = 'productos'
	queryset = Producto.objects.all()



def crearProducto(request):
	if request.method == 'POST':
		producto_form = ProductoForm(request.POST)
		if producto_form.is_valid():
			producto_form.save()
			return redirect('index')
	else:
		producto_form = ProductoForm()
		return render(request,'inventario/crear_producto.html',{'producto_form':producto_form})

def listarProducto(request):
	productos = Producto.objects.all()
	return render(request,'inventario/listar_producto.html',{'productos':productos})

def editarProducto(request,codigo):
	producto_form = None
	error = None
	try:
		producto = Producto.objects.get(codigo = codigo)
		if request.method == 'GET':
			producto_form = ProductoForm(instance = producto)
		else:
			producto_form = ProductoForm(request.POST, instance = producto)
			if producto_form.is_valid():
				producto_form.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error = e
	return render(request,'inventario/crear_producto.html',{'producto_form':producto_form,'error':error})

def eliminarProducto(request,codigo):
	producto = Producto.objects.get(codigo = codigo)
	if request.method == 'POST':
		producto.delete()
		return redirect('inventario:listar_producto')
	return render(request,'inventario/eliminar_producto.html',{'producto':producto})