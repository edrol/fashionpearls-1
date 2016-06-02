from django.contrib import admin
from customer.models import Customer
from common.models import Phone, Address

class AddressAdmin(admin.TabularInline):
    model = Address
    extra = 1

class PhoneAdmin(admin.TabularInline):
    model = Phone
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('nit', 'name', 'last_name')
    list_filter = ('gender',)
    list_display = ('name', 'last_name', 'gender', 'birthday', 'nit')
    inlines = (AddressAdmin,PhoneAdmin)



admin.site.register(Customer,CustomerAdmin)
# Register your models here.
