from django.contrib import admin
from.models import Producto

# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__str__", "stock", "precio"]
	class Meta:
		model = Producto

admin.site.register(Producto, AdminRegistrado)
