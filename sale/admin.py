from django.contrib import admin
from sale.models import Sale_S, Sales_Detail


class Sale_Online(admin.TabularInline):
    model = Sales_Detail
    extra = 1

class SalesAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'customer', 'employee', 'date',)
    inlines = (Sale_Online,)

class DetailAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity', 'sub_total',)
    list_filter = ('product',)

admin.site.register(Sales_Detail, DetailAdmin)
admin.site.register(Sale_S, SalesAdmin)
