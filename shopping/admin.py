from django.contrib import admin
from shopping.models import Buy, Purchase_Detail


class Purchase_Online(admin.TabularInline):
    model = Purchase_Detail
    extra = 1

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'provider', 'date',)
    inlines = (Purchase_Online,)

class DetailAdmin(admin.ModelAdmin):
    list_display = ('buy', 'product', 'quantity', 'cost', 'sub_total')
    list_filter = ('product',)

admin.site.register(Purchase_Detail, DetailAdmin)
admin.site.register(Buy, PurchaseAdmin)
