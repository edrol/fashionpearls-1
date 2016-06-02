from django.contrib import admin
from calculo.models import Movimiento
from django.utils.safestring import mark_safe


class MovAdmin(admin.ModelAdmin):
    fieldsets = (
        ('hola',{
            'fields':('cantidad','precio')
        }),
        ('opciones',{
            'classes':('collapse',),
            'fields':('comision',),
        }),
    )
    list_display = ("cantidad", "precio", "comision","Total_Venta")

admin.site.register(Movimiento,MovAdmin)
# Register your models here.
