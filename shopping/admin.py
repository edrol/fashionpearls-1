from django.contrib import admin
from shopping.models import Buy, Purchase_Detail


class Purchase_Online(admin.TabularInline):
    model = Purchase_Detail
    extra = 1

class PurchaseAdmin(admin.ModelAdmin):
    inlines = (Purchase_Online,)

admin.site.register(Buy, PurchaseAdmin)
# Register your models here.
