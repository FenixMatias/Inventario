"""Apirest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from inventario.views import Inicio,CrearProductoAPI,VistaProductoClienteAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')),
    path('inventario/',include(('inventario.urls','inventario'))),
    path('inicio/',Inicio.as_view(), name = 'index'),
    path('CrearProductoAPI/',CrearProductoAPI.as_view(), name = 'Crear_ProductoAPI'),
    path('VistaProductoClienteAPI/',VistaProductoClienteAPI.as_view(), name = 'Vista_Producto_ClienteAPI')
]
