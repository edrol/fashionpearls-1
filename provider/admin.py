from django.contrib import admin
from provider.models import Provider
from common.models import Phone, Address

class AddressAdmin(admin.TabularInline):
    model = Address
    extra = 1

class PhoneAdmin(admin.TabularInline):
    model = Phone
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('nit', 'name', 'last_name')
    list_filter = ('gender',)
    list_display = ('name', 'last_name', 'gender', 'birthday', 'nit')
    inlines = (AddressAdmin,PhoneAdmin)



admin.site.register(Provider,EmployeeAdmin)
# Register your models here.
