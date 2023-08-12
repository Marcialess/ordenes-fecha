from django.contrib import admin
from tienda.models import Orden, Producto, Detalle

class DetalleInLine(admin.StackedInline):
    model = Detalle
    extra = 0


class OrdenAdmin(admin.ModelAdmin):
    list_display = ("cliente", "direccion")
    inlines =[DetalleInLine]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","precio")

class DetalleAdmin(admin.ModelAdmin):
    list_display = ("orden_link","product_link",
    "cantidad","precio","subtotal")

    exclude = ["precio"]

    def save_model(self, request, obj, form, change):
        obj.precio = obj.producto.precio

        super().save_model(request,obj,form,change) # continue trabajando

    def subtotal(self,obj):
        return obj.precio * obj.cantidad

    def product_link(self,obj):
        return obj.producto.nombre

    product_link.short_description = "Producto"   

    def orden_link(self,obj):
        return obj.orden.cliente

    orden_link.short_description = "Orden"    

admin.site.register(Orden,OrdenAdmin)            
admin.site.register(Producto,ProductoAdmin)            
admin.site.register(Detalle,DetalleAdmin)            
