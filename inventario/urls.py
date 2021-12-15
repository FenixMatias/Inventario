from django.urls import include,path
from .views import crearProducto,listarProducto,editarProducto,eliminarProducto,ListadoProducto
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('crear_producto/',crearProducto, name = 'crear_producto'),
	path('listar_producto/',ListadoProducto.as_view(), name = 'listar_producto'),
	path('editar_producto/<int:codigo>',editarProducto, name = 'editar_producto'),
	path('eliminar_producto/<int:codigo>',eliminarProducto, name = 'eliminar_producto')
]