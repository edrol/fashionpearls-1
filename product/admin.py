from django.contrib import admin
from product.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter =  ('name',)
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('code', 'name')
    list_filter = ('category','cost')
    list_display = ('code', 'category', 'name', 'cost', 'sale', 'quantity', 'active','price_total')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

# Register your models here.
