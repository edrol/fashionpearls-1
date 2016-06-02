from django.contrib import admin
from calculo.models import Movimiento
from django.utils.safestring import mark_safe


class MovAdmin(admin.ModelAdmin):
    '''fieldsets = (
        ('hola',{
            'fields':('cantidad','precio')
        }),
        ('opciones',{
            'classes':('collapse',),
        }),
    )'''
    list_display = ("cantidad", "precio", "Total_Venta")

admin.site.register(Movimiento,MovAdmin)
# Register your models here.
